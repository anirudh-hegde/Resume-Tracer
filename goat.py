"""Python goat file implements the streamlit app called
   as Resume-Tracer which indentifies keywords required
"""
import cProfile
from pypdf import PdfReader
import streamlit as st

# create a empty string
page_content = ""


# function to extract the page contents of resume
def display_context_file(upload_file):
    """Extracts the page contents of a resume PDF."""
    pdf_reader = PdfReader(upload_file)

    for i, _ in enumerate(pdf_reader.pages):
        page_obj = pdf_reader.pages[i]
        page_content = str(page_obj.extract_text())

    return page_content


def main():
    """Contributes to the process of uploading the resume
    in pdf/doc/docx format and searching the keywords"""
    st.title("Resume Search App")
    upload_files = st.sidebar.file_uploader("upload your resume", type=['docx', 'pdf'])

    # if file is uploaded process will satisfy
    if upload_files:
        st.success("Resume uploaded successfully")

        # pass the uplaod_files
        page_content = display_context_file(upload_files)
        search_text = st.text_input("Enter the text which you want to search: ")

        # for input/s
        if search_text:
            st.header("Searching results..")

            for word in search_text.split(","):
                punctuations = [".", ".", "-", "*", "/"]
                for p in punctuations:
                    word = word.lower().replace(p, "")
                    page_content = page_content.lower().replace(p, "")
                if word in page_content:
                    st.success(f"{word.capitalize()} present in the resume")
                else:
                    st.error(f"{word.capitalize()} isn't present in the resume")

    else:
        st.warning("Please upload the file format only in pdf/docx")


if __name__ == "__main__":
    cProfile.run('main()')

# end of code