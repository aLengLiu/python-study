import json
from django.http import HttpResponse

from swiper.common import status_code as STATUS


def render_json(data, code=STATUS.STATUS_OK):
  result = {
    'code': code,
    'data': data
  }
  json_str = json.dumps(result, ensure_ascii=False,indent=2, sort_keys=True)
  return HttpResponse(json_str)