#-*- coding:utf-8 -*-
import os ,sys,platform
#先添加环境变量,才可以正常引用其他的包
'''
if platform.system()=='Windows':
    BASE_DIR='\\'.join(os.path.abspath(os.path.dirname(__file__).split('\\')[:-1]))
    print BASE_DIR
else:
    BASE_DIR='/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
'''
BASE_DIR="C:\Users\YXL\Desktop\project\madking1\MadKingClient"
sys.path.append(BASE_DIR)
#print(sys.path)
from core import HouseStark

if __name__=='__main__':
    HouseStark.ArgvHandler(sys.argv)