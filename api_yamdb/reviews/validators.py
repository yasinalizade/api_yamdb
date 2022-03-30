from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_score(score: int):
    """Валидация оценки."""
    if score > 10:
        raise ValidationError(
            _('%(score)s is more than 10'),
            params={'score': score},
        )
    if score < 1:
        raise ValidationError(
            _('%(score)s is less than 1'),
            params={'score': score}
        )