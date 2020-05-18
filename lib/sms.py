import random
import string
import time
import json

import requests

from worker import call_by_worker
from django.core.cache import cache
from swiper.config import HY_APP_Id, HY_APP_Key, HY_SMS_URL


def gen_verify_code(length=4):
  '''产生验证码'''
  random_list = string.digits
  sms_code = ''.join(random.choices(random_list, k=length))
  return sms_code

@call_by_worker
def send_verify_code(phone):
    '''发送验证码'''
    code = gen_verify_code()
    print('您的验证码是：%s。请不要把验证码泄露给其他人。' % code)
    data = {
        'account': HY_APP_Id,
        'password': HY_APP_Key,
        'mobile': phone,
        'format': 'json',
        'time': int(time.time()),
        'content': '您的验证码是：%s。请不要把验证码泄露给其他人。' % code
    }
    #res = requests.post(HY_SMS_URL, data=data)
    res = {}
    res['text'] = json.dumps({
        'code': 2
    })
    if (json.loads(res.get('text')).get('code') == 2):
      cache.set('VerifyCode-%s' % phone, code, timeout=600)
      print(222,res,)
      return True
    return False

@call_by_worker
def check_vode(phone, code, type):
  '''检查验证码'''
  cache_code = 0
  if type == 1:
    print('VerifyCode-%s' % phone)
    cache_code = cache.get('VerifyCode-%s' % phone)
  else:
    pass
  return cache_code == code



