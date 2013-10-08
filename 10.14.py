#!/usr/bin/python
# coding:utf-8

import os 
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/home/v/.vimrc', '/home/v/.bashrc']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something
# like that

# 2. The backup must be stored in a main backup directory
target_dir = '/home/v/' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime("%Y%m%d")
# The current time is the name of the zip archive
now = time.strftime("%H%M%S")

# Take a comment from the user to create the name of the zip file
comment = raw_input("Enter a comment --> ")
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.tar.gz'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar.gz'
# 用来替换注释中的空格，这样文件名会更容易处理
# today = '/home/v/'+ time.strftime('%Y%m%d') # 文件夹
# os.sep = '/'
# now = time.strftime("%H%M%S") # 当前时间
# '_' = '_'
# comment.replace(' ', '_') # 用_来替换注释中的空格


# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successfully created directory', today

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
tar = 'tar -cvzf %s %s' %(target, ' '.join(source))

# Run the backup
if os.system(tar) == 0:
    print 'Successful backup to', target
    os.remove(target)
else:
    print 'Backup FAILED'
