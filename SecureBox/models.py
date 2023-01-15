from django.db import models

from lib.common_model import BaseModel


from django.utils.translation import  gettext_lazy as _

from Employee.models import Employee


class SecureBox(BaseModel):

    personal_id =models.ForeignKey(
        Employee, on_delete=models.CASCADE
    )

    password = models.CharField(_('password'), default='', max_length=100)

    activation_status = models.BooleanField(
        _('status'),default=False
    )
    # applied_parts = models.

    class Meta:
        db_table = 'securebox'
        verbose_name = 'SecureBox'
        verbose_name_plural = 'SecureBoxes'
