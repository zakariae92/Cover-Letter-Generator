import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import docx2txt

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
    }
    textarea {
        height: 80vh !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Cover Letter Generator")

resume = st.file_uploader("Upload your resume", type=["pdf", "docx"])

job_description_link = st.text_input("Enter the job description link")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

if st.button("Generate Cover Letter"):
    if resume and job_description_link:
        st.success("Generating your cover letter...")

        if resume.type == "application/pdf":
            resume_content = extract_text_from_pdf(resume)
        elif resume.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_content = extract_text_from_docx(resume)
        else:
            st.error("Unsupported file type.")
            resume_content = None

        if resume_content:
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates cover letters."},
                    {"role": "user", "content": f"Here is my resume: {resume_content}. The job description is at this link: {job_description_link}. Please generate a cover letter based on this information. Start directly the cover letter without any 'here is the cover you asked ...'"}
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )

            generated_content = completion.choices[0].message.content

            st.text_area("Generated Cover Letter", value=generated_content, height=400)
    else:
        st.error("Please upload your resume and enter a job description link.")
