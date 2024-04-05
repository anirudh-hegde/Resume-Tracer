import streamlit as st

from pypdf import PdfReader
import cProfile
# craete a empty string
Page_Content = ""


# function to extract the page contents of resume
def display_context_file(upload_file):
    global page_content
    Pdfreader = PdfReader(upload_file)

    for i in range(len(pdfReader.pages)):
        PageObj = pdfReader.pages[i]
        Page_Content = str(PageObj.extract_text())

    return Page_Content


def main():
    st.title("Resume Search App")
    upload_files = st.sidebar.file_uploader("upload your resume", type=['docx', 'pdf'])

    # if file is uploaded process will satisfy
    if upload_files:
        st.success("Resume uploaded successfully")

        # pass the uplaod_files
        Page_Content = display_context_file(upload_files)
        Search_Text = st.text_input("Enter the text which you want to search: ")

        # for input/s
        if Search_Text:
            st.header("Searching results..")

            for word in Search_Text.split(","):
                punctuations = [".", ".", "-", "*", "/"]
                for p in punctuations:
                    word = word.lower().replace(p, "")
                    Page_Content = Page_Content.lower().replace(p, "")
                if word in Page_Content:
                    st.success(f"{word.capitalize()} present in the resume")
                else:
                    st.error(f"{word.capitalize()} isn't present in the resume")

    else:
        st.warning("Please upload the file format only in pdf/docx")


if __name__ == "__main__":
    cProfile.run('main()')
