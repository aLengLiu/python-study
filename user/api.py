

# Create your views here.
from lib.http import render_json

from user.models import User

# 发送验证码
from lib.sms import send_verify_code, check_vode
from swiper.common import status_code as STATUS


def get_verify_code(request):
  phone = request.GET.get('phone')
  if phone and len(str(phone)) == 11:
    if send_verify_code(phone):
      data = {'msg': '验证码发送成功，注意查收'}
      return render_json(data)
    else:
      return render_json({'msg': '验证码发送失败'}, STATUS.STATUAS_SERVICE_ERROR)
  else:
    return render_json({'msg': '请输入手机号码'}, STATUS.STATUAS_INPUT_ERROR)


def login(request):
  phone = request.POST.get('phone')
  code = request.POST.get('code')
  data = {}
  status_code = STATUS.STATUS_OK
  if check_vode(phone, code, 1):
    user, created = User.objects.get_or_create(phone=phone)
    data['userInfo'] = user.to_dict()
    data['msg'] = '登录成功'
    request.session['uid'] = user.id
  else:
    data['msg'] = '验证码验证失败'
    status_code = STATUS.STATUAS_INPUT_ERROR

  return render_json(data,status_code)


def show_profile(request):
  return render_json()


def modify_profile(request):
  return render_json()


def upload_avatar(request):
  return render_json()

