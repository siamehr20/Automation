import datetime

import khayyam
from django.db import models
from django.utils.translation import gettext_lazy as _
from khayyam import JalaliDatetime


class BaseModel(models.Model):
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    modified_time = models.DateTimeField(_('modified time'), auto_now=True)

    class Meta:
        abstract = True


class Constants:
    DEPARTMENTS = [
        (1, 'Administrator'),
        (2, 'Financial'),
        (3, 'Preservation'),
        (4, 'Tecnical'),
        (5, 'Procurement'),
        (6, 'Transport'),
        (7, 'Public Relation'),
        (8, 'Sevice')
    ]
    JOBS = []

    GENDER = [
        (1, 'Male'),
        (2, 'Female'),
        (3, 'TransGender'),
        (4, 'Undefined')
    ]

    SALARY_STATUS = [
        (1, 'In Flow'),
        (2, 'Blocked'),
        (3, 'Disconnection')
    ]

    TICKET_PRIORITY = [
        (1, 'اضطراری'),
        (2, 'خیلی مهم'),
        (3, 'مهم'),
        (4, 'عادی')
    ]

    TICKET_STATUS = [
        (0, 'بدون وضعیت'),
        (1, 'بسته'),
        (2, 'باز'),
        (3, 'دریاف شده'),
        (4, 'پیشنویس')
    ]
