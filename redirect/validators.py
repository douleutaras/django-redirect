# coding=utf-8
import re

from django.core.exceptions import ValidationError


def validate_regex(value):
    """Checks that value is a valid regex"""
    try:
        re.compile(value)
    except re.error as exc:
        raise ValidationError('%s' % exc)
