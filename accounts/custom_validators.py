from django.core.exceptions import ValidationError
from datetime import date


def validate_age(value):
    today = date.today()
    age = (
        today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    )
    if age < 12:
        raise ValidationError("You must be at least 12 years old to register.")
