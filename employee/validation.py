import re
from django.core.exceptions import ValidationError

emial_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def Email_validator(email):
    # pass the regular expression
    # and the string in search() method
    if (re.search(emial_regex, email)):
        return True

    else:
        return False





phone_number_regx = '^\+?1?\d{9,15}$'


def Phone_number_validator(phone_no):

    if(re.search(phone_number_regx,phone_no)):

        ValidationError("Valid phonenumber for".format(phone_no))
    else:
        ValidationError("Invalid Phonenumber for ".format(phone_no))

