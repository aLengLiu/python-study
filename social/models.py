from django.db import models

# Create your models here.

class Swiped(models.Model):
  '''滑动记录'''
  FLAGS = (
    ('superlike', '上滑'),
    ('like', '左滑'),
    ('dislike', '右滑'),
  )
  uid = models.IntegerField(verbose_name='滑动者的UID')
  sid = models.IntegerField(verbose_name='被滑动者的UID')
  flag = models.CharField(max_length=10, choices=FLAGS)
  dtime = models.DateTimeField(auto_now=True)

  @classmethod
  def like(cls, uid, sid):
    obj = cls.objects.create(uid=uid, sid=sid, flag='like')
    return obj

  @classmethod
  def superlike(cls, uid, sid):
    obj = cls.objects.create(uid=uid, sid=sid, flag='superlike')
    return obj

  @classmethod
  def dislike(cls, uid, sid):
    obj = cls.objects.create(uid=uid, sid=sid, flag='dislike')
    return obj

  @classmethod
  def is_liked(cls, uid, sid):
    return cls.objects.filter(uid=uid, sid=sid, flag__in=['like', 'superlike']).exists()

  @classmethod
  def like_me(cls, uid):
    cls.objects.filter(sid=uid, flag__in=['superlike', 'like'])


class Friend(models.Model):
  '''好友关系'''
  uid1 = models.IntegerField()
  uid2 = models.IntegerField()

  @classmethod
  def make_friend(cls, uid1, uid2):
    uid1, uid2 = sorted([uid1, uid2])
    cls.objects.get_or_create(uid1=uid1, uid2=uid2)

  @classmethod
  def is_friends(cls, uid1, uid2):
    uid1, uid2 = sorted([uid1, uid2])
    return cls.objects.filter(uid1=uid1, uid2=uid2).exists()

  @classmethod
  def break_off(cls, uid1, uid2):
    uid1, uid2 = sorted([uid1, uid2])
    cls.objects.filter(uid1=uid1, uid2=uid2).delete()
