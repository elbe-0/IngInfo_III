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


@pytest.mark.add
def test_can_add_country(plan):
    plan.add("france")
    assert "france" in plan.get_reiseziele()


@pytest.mark.add
def test_add_country_increases_size_of_plan(plan):
    plan.add("france")
    assert plan.size() == 1


@pytest.mark.add
def test_should_raise_error(plan):
    for i in ["England", "Austria", "Germany", "France", "Switzerland"]:
        plan.add(i)
    with pytest.raises(OverflowError):
        plan.add("france")


@pytest.mark.add
def test_should_raise_error_if_country_already_in_plan(plan):
    plan.add("france")
    with pytest.raises(ValueError):
        plan.add("france")


@pytest.mark.remove
def test_can_remove_country(plan):
    plan.add("france")
    plan.remove("france")
    assert "france" not in plan.get_reiseziele()


@pytest.mark.remove
def test_remove_country_decreases_size(plan):
    plan.add("france")
    plan.add("germany")
    plan.remove("france")
    assert plan.size() == 1


@pytest.mark.remove
def test_remove_nonexistent_country_raises_error(plan):
    with pytest.raises(ValueError):
        plan.remove("spain")


"""
Aufgabe:
- Land entfernen
- Land darf nur 1 Mal in der Liste enthalten sein
"""
