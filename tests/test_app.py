"""This file tests the streamlit app"""
from streamlit.testing.v1 import AppTest


def test_app_error():
    """tests any error occurs during testing the code of streamlit app"""
    at = AppTest.from_file("goat.py").run()
    assert not at.exception

# end of code
