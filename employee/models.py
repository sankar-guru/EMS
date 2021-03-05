from django.db import models
from django.utils.translation import gettext as _
from .validation import Email_validator,Phone_number_validator
from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
from django.core.validators import EmailValidator

# Create your models here.

emailvalidator = EmailValidator(message="invalid email")



class Employee(models.Model):

    first_name = models.CharField(_("first Name"), max_length=50,blank=True,null=True)
    last_name = models.CharField(_("last Name"),max_length=20,blank=True,null=True)
    username = models.CharField(_("username"),max_length=20,blank=True,null=True)
    phone_no = models.CharField(_("phoneno"),max_length=16,validators=[Phone_number_validator],blank=True,null=True)
    email = models.CharField(_("Email"),max_length=25,unique=True,validators=[emailvalidator],blank=True,null=True)
    description = models.TextField(_("Description"))
    status = models.BooleanField(_("Status"),default=True)



    def __str__(self):

       return self.username



