# -*- coding: utf-8 -*-
import os
import shutil
a = open("output.txt", "w")
for path, subdirs, files in os.walk(os.getcwd()):
   for filename in files:
     f = os.path.join(path, filename)
     if f.endswith(".jpg"):
      shutil.copy2(f, 
