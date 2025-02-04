#include the nessacary libraries
from openai import OpenAI
from markdown import Markdown
from dotenv import load_dotenv
import os

#my API key for openAI's chatGPT.
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") 

#reads in the resume using the markdown library
filePath = r'C:\Users\ottoh\Documents\python\resumes\OttoRes.md'
with open(filePath, 'r')as file:
    inputResume = file.read()

#input the job description for the job that you are applying for.
jobDescripition = input()

#Prompt which the LLM will recieve and use to optimize my resume for entry level software engineering jobs and internships
prompt = lambda inputResume , jobDescription : f"""
You are a Professional in resume optimization for entry-level software engineering jobs and internships.

Your task is to take a given resume and job description and enhance the resume to maximize alignment with the role while maintaining authenticity. 
Ensure that the resume highlights relevant skills, projects, coursework, and experiences that match the job description.

Optimization Guidelines:
1. Job Alignment:
Extract key qualifications, programming languages, and technical skills from the job description.
Ensure the resume reflects these skills using the candidate's real experience (projects, internships, coursework, or certifications).
Where possible, emphasize achievements with measurable impact (e.g., "Developed a web app that improved process efficiency by 20%").
2. Formatting & Readability:
Use a clean, professional layout with clear sectioning (e.g., "Education," "Projects," "Experience," "Skills").
Maintain concise bullet points following the action-verb + task + result structure.
Ensure the resume is ATS-friendly (avoid tables, images, or complex formatting).
3. Authenticity & Enhancement:
Do not fabricate information. Instead, refine and optimize existing content for clarity and impact.
Use strong action verbs (e.g., "Designed," "Implemented," "Optimized") and quantifiable achievements when applicable.
Ensure error-free grammar, spelling, and punctuation.

Input:
My Resume:
{inputResume}

The Job Description:
{jobDescripition}

Output:
1. Tailored Resume:  
A resume in Markdown format that emphasizes relevant experience, 
skills, and achievements.  
Incorporates job description keywords to optimize for ATS.  
Uses strong language and is no longer than one page.

2. Additional Suggestions (if applicable):  
List skills that could strengthen alignment with the role.  
Recommend certifications or courses to pursue.  
Suggest specific projects or experiences to develop.
"""



