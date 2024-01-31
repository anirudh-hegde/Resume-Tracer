# 🧾️Resume Tracer👁️

Resume tracer is an Streamlit App which helps the user to upload the resume in PDF/DOC format. 
After uploading, you get search bar to search for the keyword/s present in resume or not. 
Then if the keywords/s are present or not present it displays it to you.

## Demo
[Screencast from 2023-12-24 17-19-50.webm](https://github.com/anirudh-hegde/resume-tracer/assets/105560839/702413da-5832-4300-8194-0a1426b629b2)


## Tech Stacks
- Python
- Streamlit
- PyPDF2

## Prequisites
- Install Python
- Install Pycharm CE

## Build Intructions 
- Clone the repository
```sh
git clone https://github.com/anirudh-hegde/resume-tracer.git
```
- Move to repository directory
```sh
cd resume-tracer
```
- Build Docker Container 
```sh
docker build -t resutracer  .
```
- Use the container and activate the API 
```sh
docker run --user=root resutracer
```

## Conclusion
Congratulations! You have successfully run the application 🚀️.
