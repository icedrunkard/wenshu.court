#coding:utf-8

import execjs
from wenshu.attachments.jswenshu import base_64,md5,sha1,js_strToLong,js

p = execjs.compile(base_64+sha1+md5+js_strToLong+js)
p2 = execjs.compile(
    """    var createGuid = function () {return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);}""")

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
            if not intervals:
                continue
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
        if intervals[0]['IntValue']==0:#在地域分类时，最高法院即使没有没有案件也会被列出，其他则不会
            intervals=intervals[1:]
        print('将按[  {}；{}  ]分类：'.format(parent[3]['Key'],caseType),intervals[0])
        return (parent[3]['Key'],intervals)#type:'List'

