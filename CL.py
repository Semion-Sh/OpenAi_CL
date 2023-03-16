import pandas as pd
import openai
import re
from CV_duties import cv_sample, prompts_cv

openai.api_key = "your api key"

# Data from user
skils = 'SQL, Python, BigB, Data Visualization'
last_position = "Business Analyst"
years_experience = '7'
COMPLETIONS_MODEL = "text-davinci-003"

# Experience -----------------------------------------------------------------
experience_prompt = pd.read_csv('data/CL_Exp_New.csv', skipfooter=17, engine='python')


def create_request_experience(params):
    return f'Company name, where you are working: {params["Company name"]}\n' + \
        f'Your position at company where you worked: {params["Position"]}\n' + \
        f'How many years do you work in this company: {params["Years of Experience"]}\n' + \
        f'Level of your last position: {params["Grade"]}\n' + \
        f'Industry, where you worked on your position: {params["Industry"]}\n' + \
        f'Achievements and duties that you had on your position in company: {params["Achievements"]}\n' + \
        f'''Generate a winning description of the experience of the person for a Cover Letter, 
        incorporating the years of experience, position, company, industry, achievements: {params["Experience"]}\n'''


experience_cv = []
for _, row in experience_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_experience(row)
    experience_cv.append(sample)

request_experience = {
    "Company name": "Google",
    "Position": last_position,
    "Years of Experience": years_experience,
    "Grade": "Senior",
    "Industry": "It",
    "Achievements": cv_sample,
    "Experience": ""
}

quality_exp = create_request_experience(request_experience)
experience_cv.append(quality_exp)
exp_fewshot = "\n\n".join(experience_cv)

experience_request = openai.Completion.create(
    prompt=exp_fewshot,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    n=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
).choices[0]["text"].strip(" \n")

final_experience = re.sub(r"([\.!?])[^\.!?]*$", r'\1', experience_request)
# print(experience)

# Why me -----------------------------------------------------------------

why_me_prompt = pd.read_csv('data/CLsplitted-Data.csv', skipfooter=699, engine='python')


def create_request_why_me(params):
    return f'Years of experience: {params["Years of experience"]}\n' + \
        f'Company that you applied for: {params["Company that you applied for"]}\n' + \
        f'Position that you apply for: {params["Position that you apply for"]}\n' + \
        f'Company where you worked previously: {params["Company where you worked previously"]}\n' + \
        f'Your last position at your last company where you worked: {params["Your last position at your last company where you worked"]}\n' + \
        f'Skills: {params["Skills"]}\n' + \
        f'''Generate a winning description of the why company should choose me for a Cover Letter, without greeting, but describing their strengths, on behalf of the employee,
        incorporating the years of experience, Company that you applied for, Position that you apply for, Company where you worked previously, Your last position at your last company where you worked, Skills: {params["Why me"]}\n'''


why_me_cv = []
for _, row in why_me_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_why_me(row)
    why_me_cv.append(sample)

request_why_me = {
    "Years of experience": years_experience,
    "Company that you applied for": "Apple",
    "Position that you apply for": "Business Analyst",
    "Company where you worked previously": "Google",
    "Your last position at your last company where you worked": last_position,
    "Skills": skils,
    "Why me": ""
}

quality_why_me = create_request_why_me(request_why_me)
why_me_cv.append(quality_why_me)
why_me_fewshot = "\n\n".join(why_me_cv)

why_me = openai.Completion.create(
    prompt=why_me_fewshot,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    n=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
).choices[0]["text"].strip(" \n")

final_why_me = re.sub(r"([\.!?])[^\.!?]*$", r'\1', why_me)

# Why company -----------------------------------------------------------------

why_company_prompt = pd.read_csv('data/CLsplitted-Data.csv', skipfooter=500, engine='python')


def create_request_why_company(params):
    return f'Company that you applied for: {params["Company that you applied for"]}\n' + \
        f'''Generate a winning description of the why company for a Cover Letter,
        incorporating Company that you applied for: {params["Why company"]}\n'''


why_company_cv = []
for _, row in why_company_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_why_company(row)
    why_company_cv.append(sample)

request_why_company = {
    "Company that you applied for": "Apple",
    "Why company": ""
}

quality_why_company = create_request_why_company(request_why_company)
why_company_cv.append(quality_why_company)
why_company_fewshot = "\n\n".join(why_company_cv)

why_company = openai.Completion.create(
    prompt=why_company_fewshot,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    n=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
).choices[0]["text"].strip(" \n")

final_why_company = re.sub(r"([\.!?])[^\.!?]*$", r'\1', why_company)

cl = final_experience + '\n ' + final_why_me + '\n ' + final_why_company
print(cl)
