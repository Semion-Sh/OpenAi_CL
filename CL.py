import pandas as pd
import openai
import re

# openai.api_key = "your api key"

COMPLETIONS_MODEL = "text-davinci-003"

# Data from user
skils = "SQL, Python, BigB, Data Visualization"
last_position = "Business Analyst"
years_experience = "7"
previously_company = "Google"
company_apply_for = "Apple"
position_apply_for = "Business Analyst"
grade = "senior"
industry = "IT"

# Achievements -----------------------------------------------------------------
cl_prompt = pd.read_csv('data/CV_Datasets-Duties.csv')


def create_request_cl(params):
    return f'Company name, where you worked on your role: {params["Company name"]}\n' + \
        f'Your role at company where you worked: {params["Position"]}\n' + \
        f'Level of your role: {params["Grade"]}\n' + \
        f'Industry, where you worked on your role: {params["Industry"]}\n' + \
        f'''Write a winning list of the achievements and duties related for the position, 
incorporating the following features: company name, industry, grade and job role: {params["Achievements"]}\n'''


prompts_cl = []
for _, row in cl_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_cl(row)
    prompts_cl.append(sample)

# request by customer
request = {
    "Company name": previously_company,
    "Position": last_position,
    "Grade": grade,
    "Industry": industry,
    "Achievements": "",
}

quality_prompt_cl = create_request_cl(request)
prompts_cl.append(quality_prompt_cl)
achievements_fewshot = "\n\n".join(prompts_cl)

achievements_request = openai.Completion.create(
    prompt=achievements_fewshot,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    n=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
).choices[0]["text"].strip(" \n")

final_achievements = re.sub(r"([\.!?])[^\.!?]*$", r'\1', achievements_request)

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


experience_cl = []
for _, row in experience_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_experience(row)
    experience_cl.append(sample)

request_experience = {
    "Company name": previously_company,
    "Position": last_position,
    "Years of Experience": years_experience,
    "Grade": grade,
    "Industry": industry,
    "Achievements": final_achievements,
    "Experience": ""
}

quality_exp = create_request_experience(request_experience)
experience_cl.append(quality_exp)
exp_fewshot = "\n\n".join(experience_cl)

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


why_me_cl = []
for _, row in why_me_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_why_me(row)
    why_me_cl.append(sample)

request_why_me = {
    "Years of experience": years_experience,
    "Company that you applied for": company_apply_for,
    "Position that you apply for": position_apply_for,
    "Company where you worked previously": previously_company,
    "Your last position at your last company where you worked": last_position,
    "Skills": skils,
    "Why me": ""
}

quality_why_me = create_request_why_me(request_why_me)
why_me_cl.append(quality_why_me)
why_me_fewshot = "\n\n".join(why_me_cl)

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


why_company_cl = []
for _, row in why_company_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_why_company(row)
    why_company_cl.append(sample)

request_why_company = {
    "Company that you applied for": company_apply_for,
    "Why company": ""
}

quality_why_company = create_request_why_company(request_why_company)
why_company_cl.append(quality_why_company)
why_company_fewshot = "\n\n".join(why_company_cl)

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

# Why functional change
why_functional_change = pd.read_csv('data/CL_why-change.csv')

def create_request_why_change(params):
    return f'''The experience of the person for a Cover Letter, 
        incorporating the years of experience, position, company, industry, achievements: {params["Expirience"]}\n''' + \
        f'''The description of the why company should choose me for a Cover Letter on behalf of the employee,
        incorporating the years of experience, Company that you applied for, Position that you apply for, Company where you worked previously, Your last position at your last company where you worked, Skills: {params["Why me"]}\n'''+ \
        f'''The description of the why company for a Cover Letter,
        incorporating Company that you applied for: {params["Why company"]}\n''' + \
        f'''Create a winning explanation of why I decided to switch roles and how my skills matched with the new role, including the following information: Expirience, Why me, Why company: {params["Why functional change"]}\n'''

why_change_cl = []
for _, row in why_functional_change.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_why_change(row)
    why_change_cl.append(sample)


request_why_change = {
    "Expirience": final_experience,
    "Why me": final_why_me,
    "Why company": final_why_company,
    "Why functional change": '',
}

quality_why_change = create_request_why_change(request_why_change)
why_change_cl.append(quality_why_change)
why_change_fewshot = "\n\n".join(why_change_cl)

why_change = openai.Completion.create(
    prompt=why_change_fewshot,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    n=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
).choices[0]["text"].strip(" \n")

final_why_change = re.sub(r"([\.!?])[^\.!?]*$", r'\1', why_change)

final_cl = final_experience + '\n ' + final_why_me + '\n ' + final_why_company + '\n ' + final_why_change
# print(final_cl)
