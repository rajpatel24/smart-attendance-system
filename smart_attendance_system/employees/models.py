from django.db import models
from django_extensions.db.models import TimeStampedModel


class Employee(TimeStampedModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    employee_id = models.IntegerField('Employee ID')
    employee_image1 = models.ImageField('Image1', upload_to='employee/%Y/%m/%d', null=True, blank=True)
    employee_image2 = models.ImageField('Image2', upload_to='employee/%Y/%m/%d', null=True, blank=True)
    employee_image3 = models.ImageField('Image3', upload_to='employee/%Y/%m/%d', null=True, blank=True)
    employee_image4 = models.ImageField('Image4', upload_to='employee/%Y/%m/%d', null=True, blank=True)
    employee_image5 = models.ImageField('Image5', upload_to='employee/%Y/%m/%d', null=True, blank=True)
    employee_image6 = models.ImageField('Image6', upload_to='employee/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return "%s | %s | %s" % (self.pk, self.employee_id, self.user)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


class EmployeeDetectionTimeStamp(TimeStampedModel):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Employee Detection Timestamp', null=True, blank=True)

    def __str__(self):
        return "%s | %s" % (self.pk, self.employee)

    class Meta:
        verbose_name = "Employee Detection Timestamp"
        verbose_name_plural = "Employee Detection Timestamp"
