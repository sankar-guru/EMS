# Generated by Django 3.0.5 on 2021-03-03 07:30

from django.db import migrations, models
import employee.validation


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True, validators=[employee.validation.Email_validator], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='first Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='last Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_no',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[employee.validation.Phone_number_validator], verbose_name='phoneno'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='username'),
        ),
    ]
