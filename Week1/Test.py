import pytest
from Car import Car


def test1():
    t1 = Car("red", "20", "100", "50")
    assert t1.colour == "red"
    assert t1.maxSpeed == 100


def test2():
    t1 = Car("red", "20", "100", "50")
    t1.accelerate(5)
    assert t1.fuelLevel == 49


def test3():
    t1 = Car("red", "20", "100", "50")
    t1.accelerate(5)
    assert t1.currentSpeed == 25


def test4():
    t1 = Car("red", "20", "100", "50")
    t1.accelerate(85)
    assert t1.currentSpeed == 100


def test5():
    t1 = Car("red", "20", "100", "0")
    t1.accelerate(5)
    assert t1.currentSpeed == 20


def test6():
    t1 = Car("red", "20", "100", "50")
    t1.accelerate(-1)
    assert t1.currentSpeed == 20


def test7():
    t1 = Car("red", "20", "100", "50")
    t1.brake(5)
    assert t1.currentSpeed == 15


def test8():
    t1 = Car("red", "20", "100", "50")
    t1.brake(5)
    assert t1.fuelLevel == 50


def test9():
    t1 = Car("red", "20", "100", "50")
    t1.brake(25)
    assert t1.currentSpeed == 0


def test10():
    t1 = Car("red", "20", "100", "50")
    t1.brake(-1)
    assert t1.currentSpeed == 20


def test11():
    t1 = Car("red", "20", "100", "50")
    t1.refuel(5)
    assert t1.fuelLevel == 55


def test12():
    t1 = Car("red", "20", "100", "50")
    t1.refuel(100)
    assert t1.fuelLevel == 100


def test13():
    t1 = Car("red", "20", "100", "50")
    t1.refuel(-1)
    assert t1.fuelLevel == 50
