# Generated by Django 3.2.18 on 2023-10-08 05:05

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_employee_employee_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeedetectiontimestamp',
            options={'verbose_name': 'Employee Detection In Timestamp', 'verbose_name_plural': 'Employee Detection In Timestamp'},
        ),
        migrations.AlterField(
            model_name='employeedetectiontimestamp',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Employee Detection In Timestamp'),
        ),
        migrations.CreateModel(
            name='EmployeeDetectionOutTimeStamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('timestamp', models.DateTimeField(blank=True, null=True, verbose_name='Employee Detection Out Timestamp')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
            options={
                'verbose_name': 'Employee Detection Out Timestamp',
                'verbose_name_plural': 'Employee Detection Out Timestamp',
            },
        ),
    ]