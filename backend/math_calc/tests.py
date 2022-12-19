# from django.test import TestCase
import pytest


# Create your tests here.


# def test_add():
#     assert 1 == 0


@pytest.mark.urls('math_calc.urls')
def test_something(client):
    print('123123123132')
    print(client.get('/math-calc/').content)
    assert b'Success!' in client.get('/math-calc/').content
