# Cover Letter Generator

This project is a simple web application built using **Streamlit** and the **Groq API**. The application allows users to upload their resume (in PDF or DOCX format) and provide a job description link. Based on the uploaded resume and job description, the app generates a personalized cover letter using a **Large Language Model (LLM)** from Groq.

## Features

- Upload a resume in PDF or DOCX format.
- Input a link to the job description.
- Generate a customized cover letter based on the user's resume and the provided job description.
- The generated cover letter is displayed directly in the app for easy copying or editing.

## Requirements

To run the application, the following dependencies are required:

- **Python 3.7+**
- **Streamlit**
- **Groq API client**
- **PyPDF2** (for reading PDF files)
- **docx2txt** (for reading DOCX files)
- **dotenv** (for managing environment variables)

You can install the dependencies using the following command:

```bash
pip install streamlit groq PyPDF2 docx2txt python-dotenv
```

## Getting Started

1. Clone the repository:
   ```bash
    git clone https://github.com/zakariae92/cover-letter-generator.git
    cd cover-letter-generator
    ```

2. Set up your environment variables:

   - Create a .env file in the root of the project.
   - Add your Groq API key to the .env file:
   ```makefile
    GROQ_API_KEY=your-groq-api-key
    ```
3. Run the Streamlit app:
   ```bash
    streamlit run main.py
    ```
4. Open the web browser to interact with the app at:
    ```bash
    http://localhost:8501
    ```

## Usage
- Upload your resume (PDF or DOCX).
- Enter the job description link.
- Click on the Generate Cover Letter button.
- View and copy the generated cover letter in the text area displayed below.