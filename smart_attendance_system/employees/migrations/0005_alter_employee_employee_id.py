# Generated by Django 3.2.18 on 2023-10-08 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20231007_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(max_length=20, verbose_name='Employee ID'),
        ),
    ]