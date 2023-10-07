from django.db import models
from django_extensions.db.models import TimeStampedModel


class Employee(TimeStampedModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    employee_id = models.IntegerField('Employee ID', null=False, blank=False)

    def __str__(self):
        return "%s | %s | %s" % (self.pk, self.employee_id, self.user)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

