#-*-coding:utf-8-*-
"""
My first python program
"""
import re
import os
import sys
import csv
#from sys import argv
import glob
import time
output = "Tobeimport.csv"
def Main():
    curpath = os.getcwd()
    lrcfiles = curpath + "//*.lrc"
    flist = glob.glob(lrcfiles)
    writer = csv.writer(file(output, 'wb+'))
    pattern1 = re.compile(r'00]([\s\S]*) \t')
    pattern2 = re.compile(r'\t([\s\S]*)')
    i = 0
    for f in flist:
       i = i + 1
       fh = file(f,'r')
       content = fh.read()
       english = pattern1.findall(content)
       chinese = pattern2.findall(content)

       print content

       print english
       print chinese 
       mp3file = f[:-3] + "mp3"
       newname = str(time.time()) + str(i) + ".mp3"
       print mp3file
       print newname
       os.rename(mp3file, newname)
      question = chinese
          if not english:
	   answer =content[10:] +  "   
	   " +   "[sound:" + newname +"]"
           else:
	   answer = english[0] + "   " 
	   +  "[sound:" + newname +"]"
     writer.writerow([question, answer])
       fh.close()
    del writer
      
if __name__ == "__main__":
    Main()
