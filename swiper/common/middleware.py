from django.utils.deprecation import MiddlewareMixin
from lib.http import render_json
from swiper.common import status_code as STATUS
from user.models import User

class AuthMiddleware(MiddlewareMixin):
  white_list = [
    'api/user/vcode',
    'api/user/login'
  ]
  def process_request(self, request):
    path = request.path;
    if path in self.white_list:
      return
    # 用户登录验证
    uid = request.session.get('uid')
    if uid is None:
      return render_json({'msg': '用户暂未登录'}, STATUS.STATUAS_LOGIN_ERROR)
    else:
      try:
        user = User.objects.get(id=uid)
      except User.DoesNotExist:
        return render_json({'msg': '未找到该用户'}, STATUS.STATUAS_LOGIN_ERROR)
      else:
        # 将user对象添加到request
        request.user = user
