# coding=utf-8
'''
@Date: 2020-05-03 13:05:18
@LastEditTime: 2020-05-03 13:31:57
@Author: yuchonghuang@sina.cn
'''

import SplictRawData

def SplictRawDataAndCreateIndexes():
    srcFolder = '/Volumes/Data/StockAssistant/EasyStock/TradingData/临时数据/股票/'
    destFolder = '/Volumes/Data/StockAssistant/EasyStock/TradingData/RawData/股票'
    res = SplictRawData.SplitRawDataAndCreateIndex(srcFolder, destFolder)
    for date in res:
        print(date, res[date])

if __name__ == "__main__":
    SplictRawDataAndCreateIndexes()