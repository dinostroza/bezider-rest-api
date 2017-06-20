from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings
from django.core import exceptions

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    def __init__(self, *args, **kwargs):
        self._is_superuser = kwargs.get('is_superuser')
        self._is_staff     = kwargs.get('is_staff')
        super(User, self).__init__(*args, **kwargs)

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
        if self._is_staff is not None:
            return self._is_staff

        if self.id is not None:
            return self._exist_in_staffuser()

        raise ValueError('is_staff has not assigned')

    @is_staff.setter
    def is_staff(self,value):
        self._is_staff = value

    def _exist_in_staffuser(self):
        try:
            self.staffuser
        except Staffuser.DoesNotExist:
            return False
        return True

    def save_is_staff(self):
        if self._is_staff is None:
            return

        if not self._exist_in_staffuser():
            if self._is_staff:
                Staffuser(user=self).save()
        else:
            if not self._is_staff:
                self.staffuser.delete()

    @property
    def is_superuser(self):
        if self._is_superuser is not None:
            return self._is_superuser

        if self.id is not None:
            return self._exist_in_superuser()

        raise ValueError('is_superuser has not assigned')

    @is_superuser.setter
    def is_superuser(self,value):
        self._is_superuser = value

    def _exist_in_superuser(self):
        try:
            self.superuser
        except Superuser.DoesNotExist:
            return False
        return True

    def save_is_superuser(self):
        if self._is_superuser is None:
            return

        if not self._exist_in_superuser():
            if self._is_superuser:
                Superuser(user=self).save()
        else:
            if not self._is_superuser:
                self.superuser.delete()


    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.save_is_superuser()
        self.save_is_staff()


    def __str__(self):
        return self.email         


class Superuser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email

class Staffuser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email
