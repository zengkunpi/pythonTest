import random
import string
from os.path import splitext

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(code_len=4):
    """生成指定长度的验证码
    
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))
  

def get_suffix2(fileName, ignore_dor=True):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param ignore_dot: 是否忽略后缀名前面的点
    :return: 文件的后缀名
    """
    result = None
    if ignore_dor == False:
        result = splitext(fileName)[1]
    else:
        result = splitext(fileName)[1][1:] 
    return result


get_suffix2(r'C:\Users\pizen\Pictures\Screenshots\屏幕截图(1).png', ignore_dor=False)
