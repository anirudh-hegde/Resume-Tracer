"""This file tests the streamlit app"""
import os.path

from streamlit.testing.v1 import AppTest


def test_app_error():
    """tests any error occurs during testing the code of streamlit app"""
    test_dir=os.path.dirname(os.path.abspath(__file__))
    app_script_path=os.path.join(test_dir,"..","goat.py")

    assert os.path.isfile(app_script_path),f"File not found at {app_script_path}"

    at = AppTest.from_file(app_script_path).run()
    assert not at.exception
