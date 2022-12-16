import dz8

import sys

import pytest

#cage1 = dz8.Cage(300)
#cage2 = dz8.Cage(200)

#lion = dz8.Animal("Alex", 150)
#pinguin1 = dz8.Animal("Gunter", 20)
#pinguin2 = dz8.Animal("Ganter", 15)
#pinguin3 = dz8.Animal("Ginter", 25)
#begemoth = dz8.Animal("Gloria", 200)
#giraffe = dz8.Animal("Melvin", 110)
#zebra = dz8.Animal("Martin", 70)

@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (dz8.lion, True),
        (dz8.pinguin1, True),
        (dz8.pinguin2, True),
        (dz8.pinguin3, True),
        (dz8.begemoth, False),
        (dz8.giraffe, True),
        (dz8.zebra, True),

    ],
)

def test_add_animal(n, expected):
    assert dz8.cage1.add_animal(n) == expected

def test_add_animal(n, expected):
    assert dz8.cage2.add_animal(n) == expected