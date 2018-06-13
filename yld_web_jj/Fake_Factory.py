# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 0001 下午 05:37
# @Author  : Meteors.Ye
# @File    : Fake_Factory.py
# @Software: PyCharm
# 虚拟工厂


"""一些生成器方法，生成随机数，手机号，以及连续数字等"""
import random
from faker import Factory
import xlrd

fake = Factory().create('zh_CN')

def random_phone_number():
    """随机手机号"""
    return fake.phone_number()


def random_name():
    """随机姓名"""
    return fake.name()


def random_address():
    """随机地址"""
    return fake.address()

def random_ssn():
    """随机身份证"""
    return fake.ssn()

def random_card():
    """随机卡号"""
    return fake.credit_card_number(card_type=None)

def random_email():
    """随机email"""
    return fake.email()


def random_ipv4():
    """随机IPV4地址"""
    return fake.ipv4()


def random_str(min_chars=1, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)


def factory_generate_ids(starting_id=1, increment=1):
    """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids


def factory_choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
    def choice_generator():
        my_list = list(values)
        rand = random.Random()
        while True:
            yield random.choice(my_list)
    return choice_generator

def random_loanid():
    a = ['402','302']
    b = factory_choice_generator(a)()
    s = next(b)+ str(random.Random().randint(100000000000000000000000000,999999999999999999999999999))
    return s
def random_words_and_num(n=10):
    """ 返回一个n长度的随机字母+数字组合的字符串。 """
    test = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    choice_gen = factory_choice_generator(test)()
    a = ''
    for i in range(n):
        a = a + next(choice_gen)
    return a


if __name__ == '__main__':
    with open('fake.csv', mode='wb') as f:
        s = random_name() + ',' + random_ssn() + ',' + random_card() + ',' + random_address() + ',' + random_phone_number()+','+random_loanid()
        s = s.encode('utf-8')
        f.write(s)
        f.close()


















