from django.db import models
from lib.common_model import BaseModel
from Department.models import Department
from Employee.models import Employee
from django.utils.translation import gettext_lazy as _

# Create your models here.
from lib.common_model import Constants


class Ticket(BaseModel):
    uuid = models.AutoField(primary_key=True, default=1000000000)
    from_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    to_depart_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.CharField(_('subject'), max_length=150)
    context = models.TextField(_('message'))
    priority = models.SmallIntegerField(_('priority'),
                                        default=4, choices=Constants.TICKET_PRIORITY)
    attachments = models.FileField(_('attachments'), upload_to='./Ticket_Attachments',null=True)
    status = models.SmallIntegerField(_('status'),default=0, choices=Constants.TICKET_STATUS)
    is_read_by_recipient = models.BooleanField(_('is_read'), default=False)

    class Meta:
        db_table = 'tickets'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
