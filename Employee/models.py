import uuid
from collections import defaultdict

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from khayyam import JalaliDatetime
from lib.common_model import BaseModel
from lib.common_model import Constants


# class Person(BaseModel):
#     username_validator = UnicodeUsernameValidator
#     username = models.CharField(
#         _('username'),
#         primary_key=True,
#         max_length=150,
#         unique=True, help_text=('require 150 Character or Fewer'),
#         validators=[username_validator],
#         error_messages= { 'unique' :_('A username with that Already exist!')})
#
#     first_name =models.TextField(_('first_name'))
#     last_name = models.TextField(_('last_name'))
#     birthday = models.DateField(
#         _('birthday'))
#     gender = models.SmallIntegerField(
#         _('gender'),
#         choices=Constants.GENDER
#
#     )
#     national_id = models.IntegerField(
#         _('national_id'),
#     )
#     email = models.EmailField(
#         _('Email Address'),
#         blank=True)
#     address = models.TextField(
#         _('address')
#     )
#     phone_number = models.CharField(
#         _('Phone Number'),
#         max_length=11,
#         blank=True)
#
#     avatar = models.ImageField(
#         blank=True,
#         upload_to='Employee/avatar'
#     )
#
#     date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
#     account_status = models.BooleanField(_('is_active'),default=True)
#
#
#     def get_full_name(self):
#         full_name = '%s %s ' %(self.first_name, self.last_name)
#         return full_name.strip()

# class Meta:
#     # abstract = True
#     verbose_name = 'person'
#     verbose_name_plural = 'people'


class Employee(BaseModel,AbstractUser):

    @classmethod
    def generate_personal_id(cls):
        return uuid.uuid4().hex[:12]

    personal_id = models.CharField(_('personal_id'), editable=False, max_length=15,
                                   primary_key=True)
    password = models.CharField(_('password'), max_length=128)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    username_validator = UnicodeUsernameValidator
    username = models.CharField(
        _('username'),
        max_length=80,
        unique=True, help_text=('Max Characters: 80 '),
        validators=[username_validator],
        error_messages={'unique': _('A username with that Already exist!')}
    )
    first_name = models.CharField(
        _('first_name'), max_length=120,
        null=True
    )
    last_name = models.CharField(
        _('last_name'), max_length=120,
        null=True
    )
    birthday = models.DateField(
        _('birthday'),
        null=True
    )
    gender = models.SmallIntegerField(
        _('gender'),
        choices=Constants.GENDER,
        null=True
    )
    national_id = models.BigIntegerField(
        _('national_id'),
        null=True
    )
    email = models.EmailField(
        _('Email Address'),
        )
    address = models.TextField(
        _('address'), null=True
    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length=11,
        blank=True)

    avatar = models.ImageField(
        blank=True,
        upload_to='Employee/avatar'
    )

    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    account_status = models.BooleanField(_('is_active'), default=True)

    department = models.SmallIntegerField(
        _('دپارتمان مربوطه'),
        choices=Constants.DEPARTMENTS,
        null=True
    )

    job = models.SmallIntegerField(
        _('شغل'),
        choices=Constants.JOBS, null=True, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    account_activation_url = models.CharField(_('activation url'), max_length=120, null=True)
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_('code verification status'),
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        full_name = '%s %s ' % (self.first_name, self.last_name)
        return full_name.strip()

    # @property
    # def is_anonymous(self):
    #     """
    #     Always return False. This is a way of comparing User objects to
    #     anonymous users.
    #     """
    #     return False
    class Meta:
        db_table = 'employee'
        verbose_name = 'Person'
        verbose_name_plural = 'people'


pass
