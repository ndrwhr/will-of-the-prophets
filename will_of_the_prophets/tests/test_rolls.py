"""Roll tests."""

from datetime import timedelta

from django.core.exceptions import ValidationError
from django.utils import timezone

import pytest
from model_mommy import mommy


@pytest.mark.django_db
def test_must_be_later_than_latest():
    """
    Test that a roll's embargo must be after other rolls' embargoes.

    This rule needs to be in place because the create new roll page
    assumes that the roll with the latest embargo date is the most recently
    created one.
    """
    mommy.make("Roll", embargo=timezone.now() + timedelta(days=5))
    roll = mommy.prepare("Roll", embargo=timezone.now() + timedelta(days=2))
    with pytest.raises(ValidationError):
        roll.full_clean()
