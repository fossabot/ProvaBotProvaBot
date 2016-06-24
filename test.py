# -*- coding: utf-8 -*-
import os
import shutil
a = open("output.txt", "w")
for path, subdirs, files in os.walk(os.getcwd()):
   for filename in files:
     f = os.path.join(path, filename)
     if f.endswith(".jpg"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/fotoporno/")
     if f.endswith(".jpeg"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/fotoporno/")
     if f.endswith(".png"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/fotoporno/")
     if f.endswith(".mp4"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/videoporno/")
     if f.endswith(".mov"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/videoporno/")
     if f.endswith(".avi"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/videoporno/")
     if f.endswith(".m4a"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/videoporno/")
     if f.endswith(".gif"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/videoporno/")
     if f.endswith(".mpeg"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/videoporno/")
     if f.endswith(".flv"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/videoporno/")
     if f.endswith(".wmv"):
      shutil.copy2(f,"/root/ProvaBotProvaBot/videoporno/")
