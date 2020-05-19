from lib.http import render_json
from social import logic
from social.models import Swiped


def get_rcmd_user(request):
  '''获取推荐列表'''
  user = request.user
  page = int(request.GET.get('page', 1))
  per_page = 10
  start = (page - 1) * per_page
  end = start + per_page

  users = logic.rcmd_user(user)[start:end]
  result = [u.to_dict() for u in users]
  return render_json(result, 0)

def like(request):
  '''喜欢'''
  sid = int(request.GET.get('sid'))
  is_match = logic.like_someone(request.user, sid)
  return render_json({'is_match': is_match})


def superlike(request):
  '''超级喜欢'''
  sid = int(request.GET.get('sid'))
  pass


def dislike(request):
  '''不喜欢'''
  sid = int(request.GET.get('sid'))
  Swiped.dislike(request.user.id, sid)
  return render_json(None)


def rewind(request):
  '''反悔'''
  logic.rewind(request.user)
  return render_json(None)


def show_liked_me(request):
  '''查看喜欢过我的'''
  users = logic.user_liked_me(request.user)
  result = [u.to_dict() for u in users]
  return render_json({'data': result}, 0)
