# -*- coding: utf-8 -*-
import scrapy
import random
from wenshu.attachments.wenshucourt import get_guid,get_vjkl5,PreLoadSpider,p
from wenshu.attachments.dates import getDateList
from wenshu.items import WenshuItem
import json

"""
s1:GET,取得cookie中的‘vjkl5’值,最多每20次访问换一个cookie
s2:计算guid值
s3:POST,guid/vjkl5，从response得到number值
s4:加密vjkl5得到vl5x
s5:POST,guid/vl5x/vjkl5，从response得到查询内容

"""

class LcSpider(scrapy.Spider):
    name = 'lc'
    allowed_domains = ['wenshu.court.gov.cn']
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
             'Host': 'wenshu.court.gov.cn',
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
             'X-Requested-With':'XMLHttpRequest',
             }

    url_getcode='http://wenshu.court.gov.cn/ValiCode/GetCode'
    url_getcookie='http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1++%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6+%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6'
    url_listContent='http://wenshu.court.gov.cn/List/ListContent'
    url_treeContent='http://wenshu.court.gov.cn/List/TreeContent'

    dates = getDateList((2017,3,1),(2017,3,1))


    def start_requests(self):
        for date in self.dates:#每一日
            f=PreLoadSpider(date)
            count=f.count
            if count > 2000:#大于2000的需要将标签细分，以获取全部条数
                if f.optMap:#如果（第一次）有优选的分类，则按优选分类获取结果；否则在else中加入caseType，继续
                    optIntervals = f.optIntervals#此时内部已经得出优选方案，如文书类型、审判程序、法院地域等

                    for interval in optIntervals[:1]:#每个小区间
                        query = '裁判日期:{} TO {},{}:{}'.format(date, date, f.dimension, interval['Key'])#比如文书类型
                        pages=interval['IntValue']
                        # for page in range(1,1+pages):
                        for page in range(1,2):#每一页
                            yield scrapy.Request(self.url_getcookie,
                                         headers=self.headers,
                                         meta={'cookiejar':random.random(),
                                               'query':query,
                                               'page':page},
                                         dont_filter=True,
                                         callback=self.getcookie)
                else:

                    for caseType in ['刑事案件','民事案件','行政案件','赔偿案件','执行案件'][:1]:
                        f = PreLoadSpider(date, caseType)
                        optIntervals = f.optIntervals
                        for interval in optIntervals[1:2]:
                            query = '裁判日期:{} TO {},{}:{},{}:{}'.format(date, date, f.dimension, interval['Key'],'案件类型',caseType)
                            pages=interval['IntValue']
                            # for page in range(1,1+pages):
                            for page in range(1,2):#每一页
                                yield scrapy.Request(self.url_getcookie,
                                             headers=self.headers,
                                             meta={'cookiejar':random.random(),
                                                   'query':query,
                                                   'page':page},
                                             dont_filter=True,
                                             callback=self.getcookie)
            else:
                pages = int(count/20) if count%20==0 else int(count/20)+1
                query = '裁判日期:{} TO {}'.format(date, date)
                # for page in range(1,1+pages):
                for page in range(1,2):#每一页
                    yield scrapy.Request(self.url_getcookie,
                                         headers=self.headers,
                                         meta={'cookiejar':random.random(),
                                               'query':query,
                                               'page':page},
                                         dont_filter=True,
                                         callback=self.getcookie)
    def getcookie(self, response):
        #s1
        cookie_string=response.headers.get('Set-Cookie').decode()
        vjkl5=get_vjkl5(cookie_string)

        #s2
        guid = get_guid()
        print('vjkl5(from cookie):', vjkl5)
        yield scrapy.FormRequest(self.url_getcode,#访问getcode网址得到number值
                            headers=self.headers,
                            meta={
                                'cookiejar':response.meta['cookiejar'],
                                'vjkl5':vjkl5,
                                'guid':guid,
                                'query':response.meta['query'],
                                'page': response.meta['page']
                                   },
                            formdata={'guid': guid},
                            callback=self.getcode,
                            dont_filter=True
                             )
    def getcode(self,response):
        #s3
        number=response.text
        #s4
        vjkl5=response.meta['vjkl5']
        strlength = p.call('strToLong', vjkl5)
        funcIndex = strlength % 200
        func_s = 'makeKey_' + str(funcIndex)
        vl5x = p.call(func_s, vjkl5)
        #s5
        data = {
                    'Param': response.meta['query'],
                    'Index': str(response.meta['page']),
                    'Page': '20',
                    'Order': '法院层级',
                    'Direction': 'asc',
                    'vl5x': vl5x,
                    'number': number,
                    'guid': response.meta['guid']
                }
        print(number,data)
        yield scrapy.FormRequest(self.url_listContent,
                                 headers=self.headers,
                                 formdata=data,
                                 meta={'cookiejar':response.meta['cookiejar']},
                                 callback=self.parse_listContent,
                                 dont_filter=True
                                 )
    def parse_listContent(self,response):
        item=WenshuItem()
        text=response.text.replace('\\','')[1:][:-1]#去除斜杠，去除首尾的引号
        print(type(text))
        text_seq=json.loads(text)
        print(text_seq)

        for each in text_seq[1:]:
            # item['judgementKeystone'] =each.get('裁判要旨段原文')
            item['caseType'] =each.get('案件类型')
            item['judgementDate'] =each.get('裁判日期')
            item['caseName'] =each.get('案件名称')
            item['docID'] =each.get('文书ID')
            item['caseID'] =each.get('审判程序')
            item['trialProcedure'] =each.get('案号')
            item['courtName'] = each.get('法院名称')
            print(item)
            yield item





