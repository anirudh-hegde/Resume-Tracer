import streamlit as st
import PyPDF2

# craete a empty string
page_content = ""


# function to extract the page contents of resume
def display_context_file(upload_file):
    global page_content
    pdfReader = PyPDF2.PdfReader(upload_file)

    for i in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[i]
        page_content = str(pageObj.extract_text())

    return page_content


def main():
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
                    word=word.lower().replace(p,"")
                    page_content=page_content.lower().replace(p,"")
                if word in page_content:
                    st.success(f"{word.capitalize()} present in the resume")
                else:
                    st.error(f"{word.capitalize()} isn't present in the resume")

    else:
        st.warning("Please upload the file format only in pdf/docx")


if __name__ == "__main__":
    main()
