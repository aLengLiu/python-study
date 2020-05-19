import datetime

from user.models import User
from social.models import Swiped, Friend


def rcmd_user(user):
  dating_sex = user.profile.dating_sex
  location = user.profile.location
  min_dating_age = user.profile.min_dating_age
  max_dating_age = user.profile.max_dating_age

  cur_year = datetime.date.today().year
  min_year = cur_year - max_dating_age
  max_year = cur_year - min_dating_age
  users = User.objects.filter(sex=dating_sex,
                      address=location,
                      birth_year__gte=min_year,
                      birth_year__lte=max_year)
  return users


def like_someone(user, sid):
    Swiped.like(user.id, sid)
    if Swiped.is_liked(sid, user.id):
      Friend.make_friend(user.id, sid)
      return True
    return False


def rewind(user):
    s = Swiped.objects.filter(uid=user.id).latest()
    if s.flag in ['superlike', 'like']:
      # if Friend.is_friends(user.id, s.sid):
        Friend.break_off(user.id, s.sid)
    s.delete()


def user_liked_me(user):
  swipes = Swiped.like_me(user.id)
  swipes_ids = [s.uid for s in swipes]
  return User.objects.filter(id__in=swipes_ids)

