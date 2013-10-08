#!/usr/bin/python
# coding:utf-8

import os
import time

# 1. The files and directories to be backed up are specified in a list.
#source = '/home/v/.bashrc' # 只有一个路径的时候可以真么写
                           # 21行，就只写source即可
                           # 多个就要用列表source = ['/home/v/py', '/home/v/.bashrc']
                           # 21行，source就要写成' '.join(source)
source = ['/home/v/.bashrc', '/home/v/.vimrc']

# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/home/v/' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

print ' '.join(source) # 当有多个路径时，用空格来区分
# 5. We use the zip command (in Unix/Linxu) to put the files in a zip archive
zip_command = "zip -qr %s %s" %(target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
    os.remove(target) # 用python内建命令删除生成的目标文件
else:
    print 'Backup FAILED'


