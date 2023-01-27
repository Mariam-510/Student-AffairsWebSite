from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_domainonly_GPA(value):
    if value<0 or value>4:
        raise ValidationError(_("GPA is invalid"))
    return value


def validate_domainonly_id(value):
    if value < 0:
        raise ValidationError(_("ID is invalid"))
    return value


def validate_domainonly_email(value):
    if value == "":
        raise ValidationError("Email is invalid")
    return value
