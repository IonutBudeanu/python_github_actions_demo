# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import os
import pytest


@pytest.fixture(scope="session")
def my_user():
    return f"{os.environ['MY_USER']}"


@pytest.fixture(scope="session")
def my_password():
    return f"{os.environ['MY_PASS']}"


def test_credentials(my_user, my_password):
    print(f'\n>>>>> User: {my_user}, \n>>>>> Password: {my_password}')
    assert "My" in my_user and "asswo" in my_password
