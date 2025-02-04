from openai import OpenAI
from markdown import Markdown
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") 

#reads in the resume using the markdown library
filePath = r'C:\Users\ottoh\Documents\python\resumes\OttoRes.md'
with open(filePath, 'r')as file:
    inputResume = file.read()

#input the job description for the job that you are applying for.
jobDescripition = input()

prompt = lambda inputResume , jobDescription : f"""
You are an AI assistant specializing in resume optimization. Your task is to take a given resume and a job description and optimize the resume to maximize\
alignment with the job while maintaining authenticity. Ensure the resume highlights relevant skills, experience, and achievements tailored to the role.

Additionally, improve formatting for clarity, readability, and professionalism, following industry best practices. Use concise bullet points, proper \
sectioning, and a clean layout. Maintain a professional yet engaging tone.

Instructions:
Job Alignment:

Extract key qualifications and skills from the job description.
Ensure the resume reflects these qualifications using the candidate's real experience and skills.
Emphasize relevant achievements with measurable impact where possible.
Formatting & Readability:

Use consistent font, spacing, and section headers.
Ensure bullet points are clear, concise, and results-oriented.
Maintain an ATS-friendly structure (no excessive tables, images, or fancy formatting).
Authenticity & Enhancement:

Do not fabricate information. Instead, rephrase and optimize existing content.
Use strong action verbs and quantifiable achievements where applicable.
Ensure grammar, spelling, and punctuation are error-free.
Output the optimized resume in a structured format, ensuring it remains compelling and tailored for the role.
"""



