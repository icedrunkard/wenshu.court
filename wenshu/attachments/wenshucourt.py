#coding:utf-8

import requests
import execjs
from wenshu.attachments.jswenshu import base_64,md5,sha1,js_strToLong,js
import json


p = execjs.compile(base_64+sha1+md5+js_strToLong+js)
p2=execjs.compile("""    var createGuid = function () {return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);}""")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Host': 'wenshu.court.gov.cn',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    }


def get_vjkl5(cookie_string):
    for s in cookie_string.split(';'):
        if 'vjk' in s:
            return s.replace('vjkl5=','')


def get_guid():
    s=p2.call('createGuid')+p2.call('createGuid')+'-'+p2.call('createGuid')+'-'+p2.call('createGuid')+p2.call('createGuid')+'-'+p2.call('createGuid')+p2.call('createGuid')+p2.call('createGuid')
    return s

def get_OptMap(totalitems,parent,caseType):
    """
    :param total: 案件数量
    :param parent: 总分类树
    :return: tuple: 分类类型、分类区间案件数量列表
    """

    for dimension in [parent[-1],parent[-2]]:#优先测试“文书类型”、“审判程序”是否最优遍历分类
        if abs(totalitems-int(dimension['Value']))/totalitems<0.005:#如果案件数量误差小于千分之五，向下执行
            intervals=dimension['Child']
            for branch in intervals:
                if branch['IntValue']>2000:#如果某个区间中有数量大于2000的，则该维度不适宜做最优遍历，进入下一个维度
                    break
            else:
                print('将按[  {}；{}  ]分类：'.format(dimension['Key'],caseType),intervals[0])
                return (dimension['Key'],intervals)#type:'List'
        else:
            break
    else:
        intervals = parent[3]['Child']#按地域划分
        length = len(intervals)
        intervals=[intervals[branchIndex] for branchIndex in range(0,length,2)]#每个地域后面紧跟一个详情，为空字典
        for branch in intervals:
            if branch['IntValue']>2000:#如果某个区间中有数量大于2000的，则该维度不适宜做最优遍历，进入下一个维度
                return None
        else:
            print('将按[  {}；{}  ]分类：'.format(parent[3]['Key'],caseType),intervals[0])
            return (parent[3]['Key'],intervals)#type:'List'






class PreLoadSpider(object):
    def __init__(self,date,caseType=None):
        self.date=date

        self.caseType=caseType

        self.get_res(self.date,self.caseType)

    def get_res(self,date,caseType):
        url_getcode = 'http://wenshu.court.gov.cn/ValiCode/GetCode'
        url_cookie = 'http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1++%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6+%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6'
        # url_listContent = 'http://wenshu.court.gov.cn/List/ListContent'
        url_treeContent = 'http://wenshu.court.gov.cn/List/treeContent'
        res_cookie = requests.get(url_cookie, headers=headers)
        cookie_string = res_cookie.headers.get('Set-Cookie')
        vjkl5 = get_vjkl5(cookie_string)
        headers['Cookie'] = 'vjkl5=' + vjkl5

        print('vjkl5(from cookie):', vjkl5)

        strlong = p.call('strToLong', vjkl5)
        funcIndex = strlong % 200
        # print('funIndex:',funcIndex)
        func_s = 'makeKey_' + str(funcIndex)
        # print('first_called:'+func_s)
        vl5x = p.call(func_s, vjkl5)
        print('vl5x:', vl5x)

        guid = get_guid()

        res_number = requests.post(url_getcode, headers=headers, data={'guid': guid})
        print('number:', res_number.text)
        data = {
            'Param': '裁判日期:{} TO {}'.format(date, date),
            'vl5x': vl5x,
            'number': res_number.text,
            'guid': guid
        }
        if caseType:
            data['Param']='裁判日期:{} TO {},案件类型:{}'.format(date, date,caseType)
        print('data ready to post: ', data)
        res_treeContent = requests.post(url_treeContent, headers=headers, data=data)
        res_treeContent.encoding = 'utf-8'
        text=res_treeContent.text.replace('\\','')[1:-1]#去除斜杠，去除首尾的引号

        text_seq=json.loads(text)
        # print('-----------------------------',text_seq)
        self.count=int(text_seq[-3]['IntValue'])
        self.optMap=get_OptMap(self.count, text_seq,caseType)
        if self.optMap:#如果不为空，则有最优遍历方法
            self.dimension=self.optMap[0]
            self.optIntervals=self.optMap[1]
        else:#否则需重新访问
            self.optMap=None
