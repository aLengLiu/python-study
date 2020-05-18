'''定义状态码'''

# 正常
STATUS_OK = 0

#用户相关
STATUAS_INPUT_ERROR = 2001
STATUAS_LOGIN_ERROR = 2002
STATUS_FORM_ERROR = 2003 # 表单字段校验错误

# 服务相关
STATUAS_SERVICE_ERROR = 5001


class LogicError(BaseException):
  pass


def generate_logic_error(name, code):
  base_cls = (LogicError,)
  return type(name, base_cls, {'code': code})

VcodeError = generate_logic_error('STATUAS_INPUT_ERROR', 2001)