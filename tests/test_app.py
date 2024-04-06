from streamlit.testing.v1 import AppTest

def test_app_error():
    at=AppTest.from_file("goat.py").run()
    assert not at.exception

    # at.sidebar.file_uploader("Anirudh-Hegde-DevOps-Resume.pdf")
    # assert at.warning[0].value=="upload the document in pdf/doc/docx format"