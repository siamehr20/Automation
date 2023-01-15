from django.db import models
from django.utils.translation import gettext_lazy as _
from lib.common_model import BaseModel
from Employee.models import Employee


class Manager(BaseModel):
    personal_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE)

    Manager_name = models.CharField(_('نام مدیر'), max_length=130, default='',  blank=True )

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'
        db_table = 'manager'
