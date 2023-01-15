from django.db import models
from django.utils.translation import gettext_lazy as _
from Employee.models import Employee
from lib.common_model import BaseModel, Constants


class FinancialDepartment(BaseModel):

    personal_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE)

    salary_status = models.PositiveSmallIntegerField(
        _('salary_status'),
        choices=Constants.SALARY_STATUS
    )
    salary_amount = models.IntegerField(
        _('salary_amount'),

    )

    class Meta:
        db_table = 'financial'
        verbose_name = 'Financials'
        verbose_name_plural = 'Financials'

    @classmethod
    def salary_amounts(cls):
        return '{: ,.3f}'.format(cls.salary_amount)
