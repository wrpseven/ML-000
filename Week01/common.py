#coding=utf-8
import io
import traceback
import json
import math
import os
import sys



##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
## 函数部分
## get_tb_info              获取异常的细节，帮助调试代码
## show_dict_intree         以树的形式，可视化一个字典
## debug_line               调试时打印分行符，【"\t"*30 + "**"*30】 
## is_number                输入字符串,是否为数字
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def get_tb_info():
    message = traceback.format_exc()
    return message

def show_dict_intree(_input_dict):
    print(json.dumps(_input_dict, indent=2)) 

def debug_line():
    print("\t"*30)
    print("**"*30)
    return 0

def is_number(_value):
    flag = True
    try:
        c = float(_value)
        c += 1
        if math.isnan(c):
            flag = False
        else:
            flag = True
    except:
        flag = False
    return flag
