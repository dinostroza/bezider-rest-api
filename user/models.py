from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from api import settings

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email            = models.EmailField('email address', unique=True)
    username         = models.CharField('username', max_length=30, unique=True,blank=False)
    first_name       = models.CharField('first name', max_length=30, blank=True)
    last_name        = models.CharField('last name', max_length=30, blank=True)
    date_of_birth    = models.DateField('date of birth', blank=True, null=True)
    #country          = 
    #languages        = 
    self_description = models.TextField('self description', max_length=500, blank=True)
    #profile_picture  = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    points           = models.IntegerField('points', default=0, blank=True)
    rank             = models.IntegerField('rank', default=0, blank=True)
    date_joined      = models.DateTimeField('date joined', auto_now_add=True)
    is_active        = models.BooleanField('active', default=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD    = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return (self.email in settings.STAFF_EMAILS)

    # @property
    # def is_superuser(self):
    #     "Is the user a superuser of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return (self.email == 'dinostroza@gmail.com')
