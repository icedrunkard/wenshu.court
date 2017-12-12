#-*coding:utf-8
import datetime


def getDateList(start, end):#准备改成生成器
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append("%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day))
        curr_date += datetime.timedelta(1)
    result.append("%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day))
    # print(result)
    return result
# getDateList((2017,1,1),(2017,1,2))