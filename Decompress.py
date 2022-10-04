# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:42:38 2020

@author: overs
"""

import os
import time

Input_path = r'I:\解压位置'

Zip_path = r'E:\7z\x64\7za'
Rar_path = r'E:\RAR\UnRAR.exe'

Key = ('sjhs001.xyz','sjhs08.xyz','sjhs04.com') #'sjhs03.com','sjhs02.com','sjhs04.com','sjhs.pw',

#Output_root_path = r'Z:\csv数据集\视频套图'

Output_root_path = r'\\192.168.101.9\share\csv数据集\视频套图'





Time = ''
if time.localtime().tm_mon <= 9:
    Time += '0' + str(time.localtime().tm_mon)
else:
    Time +=  str(time.localtime().tm_mon)    
if time.localtime().tm_mday <= 9:
    Time += '0' + str(time.localtime().tm_mday) 
else:
    Time += str(time.localtime().tm_mday) 
Time = '2021_' + Time
T = os.listdir(Output_root_path)
Output_path = Output_root_path + '\\' + '集合' + '\\' + '最新'
#if Time not in T :
#    os.mkdir(Output_path)
    

FileName = os.listdir(Input_path)
FileName7z = [i for i in FileName if "xltd" not in i and  "7z" in i]
FileNameRar = [i for i in FileName if "xltd" not in i and "rar" in i]
FileNameBox = [os.path.join(Input_path,i) for i in FileName if os.path.isdir(os.path.join(Input_path,i))]

for filename in FileName7z:
    for key in Key:
        Status = os.system(Zip_path + ' x ' + os.path.join(Input_path,filename) + ' -p' + key + ' -o' + Output_path + ' -aos'  )
        if not Status:
            print(filename, ' success!')
            break
    if Status:
        print('filename', ' fail')


for filename in FileNameRar:
    for key in Key:
        Status = os.system(Rar_path + ' x ' + os.path.join(Input_path,filename) + ' -p' + key + " "+ Output_path )
        if not Status:
            print(filename, ' success!')
            break
    if Status:
        print('filename', ' fail')

for FileBox in FileNameBox:
    FileList = os.listdir(FileBox)
    if not FileList:
        continue
    filename = sorted(FileList)[0]
    if "rar" in filename:
        for key in Key:
            Status = os.system(Rar_path + ' x ' + os.path.join(FileBox,filename) + ' -p' + key + " " + Output_path )
            if not Status:
                print(filename, ' success!')
                break
        if Status:
            print('filename', ' fail')
    elif "7z" in filename:
        for key in Key:
            Status = os.system(Zip_path + ' x ' + os.path.join(FileBox,filename) + ' -p' + key + ' -o' + Output_path + ' -aos'  )
            if not Status:
                print(filename, ' success!')
                break
        if Status:
            print('filename', ' fail')
            
            
    