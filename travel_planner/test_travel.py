"""
Some Unit Test-basics in Python

Author: L. Bleicher
Last modified: 30.09.24

"""
import pytest

from travel import Travelplan


@pytest.fixture
def plan():
    return Travelplan()


@pytest.mark.example
def test_can_add_country(plan):
    plan.add("france")
    assert "france" in plan.get_reiseziele()


def test_add_country_increases_size_of_plan(plan):
    plan.add("france")
    assert plan.size() == 1


