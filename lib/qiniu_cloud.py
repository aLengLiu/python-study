from qiniu import Auth, put_file, etag
from swiper import config


QN_Auth = Auth(config.QN_ACCESS_KEY,config.QN_SECRET_KEY)


def upload_to_qiniu(localfile, key):
  '''
    Args:
      localfile: 本地文件位置
      key: 上传到服务器的名字
  '''

  bucket_name = config.QN_BUCKET
  token = QN_Auth.upload_token(bucket_name, key, 3600)
  ret, info = put_file(token, key, localfile)
  print(info)
  assert ret['key'] == key
  assert ret['hash'] == etag(localfile)