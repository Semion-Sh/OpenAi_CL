import openai
import pandas as pd
import numpy as np
import pickle
# from transformers import GPT2TokenizerFast
from typing import List
from CV_duties import cv_sample, prompts_cv

openai.api_key = "your api key"
COMPLETIONS_MODEL = "text-davinci-003"
# COMPLETIONS_MODEL = "text-curie-001"

archivment = openai.Completion.create(
    prompt=cv_sample,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    n=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
).choices[0]["text"].strip(" \n")


def create_request_summary(params):
    return f'Company name, where you worked on your position: {params["Company name"]}\n' + \
        f'Your position at company where you worked: {params["Position"]}\n' + \
        f'How many years do you work in this industry: {params["Years of Experience"]}\n' + \
        f'Level of your last position: {params["Grade"]}\n' + \
        f'Industry, where you worked on your position: {params["Industry"]}\n' + \
        f'Achievements and duties that you had on yor position in company: {params["Achievements"]}\n' + \
        f'''Generate a winning description of the experience of the person for a resume,
        incorporating years of experience, level of the position, position, company and industry: {params["Summary"]}\n'''


summary_prompt = pd.read_csv('data/Summary_Dataset_QA.csv')

summary_cv = []
for _, row in summary_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_summary(row)
    summary_cv.append(sample)

request_summary = {
    "Company name": "Hoff",
    "Position": "Intern UX/UI Designer",
    "Years of Experience": "0.5",
    "Grade": "Intern",
    "Industry": "E-commerce",
    "Achievements": archivment,
    "Summary": ""
}

quality_prompt_summary = create_request_summary(request_summary)
summary_cv.append(quality_prompt_summary)
summary_fewshot = "\n\n".join(summary_cv)

completion = openai.Completion.create(
    prompt=summary_fewshot,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    n=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
)
print(completion.choices[0]["text"].strip(" \n"))
