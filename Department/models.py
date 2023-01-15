from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from Employee.models import Employee
from lib.common_model import BaseModel, Constants

from Manager.models import Manager


class Department(BaseModel):
    department = models.PositiveSmallIntegerField(
        _('department_id'),
        primary_key=True,
        choices=Constants.DEPARTMENTS)

    manager = models.ForeignKey(
        Manager, on_delete=models.SET_DEFAULT, default=1
    )

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        db_table = 'department'
