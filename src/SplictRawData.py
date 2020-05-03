# coding=utf-8
'''
@Date: 2020-05-03 13:25:46
@LastEditTime: 2020-05-03 13:31:11
@Author: yuchonghuang@sina.cn
'''

import os
import shutil

def GetFolderNameByDate(date):
    year,month,_ = date.split('-')
    Quarter = (int(month)-1)//3+1
    return '%s/Q%s'%(year,Quarter)

def SplitRawData(srcFolder, destFolder):
    res = {}
    if os.path.exists(destFolder) == False:
        os.makedirs(destFolder)
    
    files = os.listdir(srcFolder)
    for file_ in files:
        fullpath = os.path.join(srcFolder, file_)
        if fullpath.find('.xls') == -1:
            continue
        date = file_[:file_.find('.')]
        resFolder = os.path.join(destFolder,GetFolderNameByDate(date))
        if os.path.exists(resFolder) == False:
            os.makedirs(resFolder)
        destFileName = os.path.join(resFolder,file_)
        shutil.move(fullpath, destFileName)
        res[date] = destFileName
    return res

def listAllFilesInFolder(folder):
    allfile=[]
    for dirpath,_,filenames in os.walk(folder):
        for name in filenames:
            allfile.append(os.path.join(dirpath, name))
    return allfile
    
def ReCreatIndexOfRawData(srcFolder):
    files = listAllFilesInFolder(srcFolder)
    res = {}
    for file_ in files:
        if file_.find('.xls') == -1:
            continue
        date = file_[file_.rfind('/')+1:file_.rfind('.xls')]
        res[date] = file_
    return res

def SplitRawDataAndCreateIndex(srcFolder, destFolder):
    SplitRawData(srcFolder, destFolder)
    return ReCreatIndexOfRawData(destFolder)