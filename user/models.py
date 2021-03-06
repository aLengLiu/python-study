import datetime

from django.db import models

# Create your models here.
from lib.orm import ModelMixin


class User(models.Model, ModelMixin):
  SEX =(
    ('男性', '男性'),
    ('女性', '女性'),
  )
  nickname = models.CharField(max_length=32, unique=True)
  phone = models.CharField(max_length=11, unique=True)
  sex = models.CharField(max_length=8, choices=SEX)

  birth_year = models.IntegerField(default=2000,verbose_name='出生年')
  birth_month = models.IntegerField(default=1,verbose_name='出生月')
  birth_day = models.IntegerField(default=1,verbose_name='出生日')

  avatar = models.CharField(max_length=256, verbose_name='头像')
  address = models.CharField(max_length=256, verbose_name='居住地')

  @property
  def age(self):
    today = datetime.date.today()
    birthday = datetime.date(self.birth_year, self.birth_month,self.birth_day)
    return (today - birthday).days // 365

  @property
  def profile(self):
    p = None
    if not hasattr(self, '_profile'):
      self._profile, _ = Profile.objects.get_or_create(id=self.id)
    return self._profile


class Profile(models.Model, ModelMixin):
  SEX = (
    ('男性', '男性'),
    ('女性', '女性'),
  )
  location = models.CharField(max_length=256, verbose_name='目标城市')
  min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
  max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
  min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
  max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
  dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配的性别')
  vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
  only_matche = models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')
  auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')

