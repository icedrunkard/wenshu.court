# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WenshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    judgementKeystone=scrapy.Field()#'裁判要旨段原文'
    caseType=scrapy.Field()#'案件类型'
    judgementDate=scrapy.Field()#'裁判日期'
    caseName=scrapy.Field()#'案件名称'
    docID=scrapy.Field()#'文书ID'
    caseID=scrapy.Field()#'审判程序'
    trialProcedure=scrapy.Field()#'案号'
    courtName=scrapy.Field()#'法院名称'
