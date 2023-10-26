'''
编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来
'''
import os
path=os.getcwd()+"\\file_data"

with open(f"{path}/data.txt","w+") as file:
    file.write("this is hello python!!!")
    file.writelines(["this is hello java!!!\n","this is hello go!!!"])
    file.seek(0)
    print(file.read(3))
    file.seek(0)
    print(file.read())
    file.seek(0)
    print(file.readlines())
print(file.closed)
