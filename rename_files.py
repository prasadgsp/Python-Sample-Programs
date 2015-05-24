import os

def rename_files():
 file_list=os.listdir(r"D:\online courses\U.D.A.C.I.T.Y\Programming Foundations with Python\prank")
 #print(file_list)
 os.chdir(r"D:\online courses\U.D.A.C.I.T.Y\Programming Foundations with Python\prank")
 for file_name in file_list:
  os.rename(file_name,file_name.translate(None,"0123456789"))
rename_files()
