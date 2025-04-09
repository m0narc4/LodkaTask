import pytest
from Boat import Boat


@pytest.fixture
def boat():
    return Boat(100)


def test_rowing(boat):
    boat.attach_oars()
    boat.move('вперёд')
    assert boat.direction == 'вперёд'
    boat.move('назад')
    assert boat.direction == 'назад'


def test_rotating(boat):
    boat.attach_oars()
    boat.move('вправо')
    assert boat.direction == 'вправо'
    boat.move('влево')
    assert boat.direction == 'влево'


def test_anchor_function(boat):
    assert boat.drop_anchor() == 'Якорь сброшен в воду'
    assert boat.drop_anchor() == 'Якорь уже сброшен в воду'
    assert boat.raise_anchor() == 'Якорь поднят'
    assert boat.raise_anchor() == 'Якорь уже поднят'
