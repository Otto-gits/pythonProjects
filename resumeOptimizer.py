from openai import OpenAI
from markdown import Markdown

filePath = '/resumes/Resume.md'

with open(filePath, 'r')as file:
    inputResume = file.read



#input the job description for the job that you are applying for.
jobDescripition = input()

print(jobDescripition)