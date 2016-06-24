import os

a = open("output.txt", "w")
for path, subdirs, files in os.walk(r'C:\Users\user\Desktop\Test_Py'):
   for filename in files:
     f = os.path.join(path, filename)
print(f)
