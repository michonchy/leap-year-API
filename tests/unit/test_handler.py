import json

import pytest

from leap_year import app


def test_is_leap_year():
    assert app.is_leap_year(400) == "leap year"
    assert app.is_leap_year(1300) == "not leap year"
