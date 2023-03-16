# create Achievements by 'Company name', 'Position', 'Grade', 'Industry'

import pandas as pd
import ttm

cv_prompt = pd.read_csv('data/CV_Datasets-Duties.csv')


# Что я делаю:
# Объявляю переменную, для чтения данных. Для CV duties

def create_request_cv(params):
    return f'Company name, where you worked on your role: {params["Company name"]}\n' + \
        f'Your role at company where you worked: {params["Position"]}\n' + \
        f'Level of your role: {params["Grade"]}\n' + \
        f'Industry, where you worked on your role: {params["Industry"]}\n' + \
        f'''Write a winning list of the achievements and duties related for the position, 
incorporating the following features: company name, industry, grade and job role: {params["Achievements"]}\n'''


# Дальше складываю все прочитанные данные из файла в лист
prompts_cv = []
for _, row in cv_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_cv(row)
    prompts_cv.append(sample)

# request by customer
request = {
    "Company name": "Google",
    "Position": "Business Analyst",
    "Grade": "senior",
    "Industry": "IT",
    "Achievements": "",
}

# Я его джойню к листу promopts_cv
# и отправляю это всё на генерацию

quality_prompt_cv = create_request_cv(request)
prompts_cv.append(quality_prompt_cv)
cv_sample = "\n\n".join(prompts_cv)
# print(cv_sample)

# generated_cv_1 = ttm.generate(cv_sample, min_tokens=20, max_tokens=30, num_hypos=5)
# generated_cv_2 = ttm.generate(cv_sample, min_tokens=20, max_tokens=30, num_hypos=5)
# generated_cv_3 = ttm.generate(cv_sample, min_tokens=2, max_tokens=30, num_hypos=5)
# generated_cv_4 = ttm.generate(cv_sample, min_tokens=2, max_tokens=30, num_hypos=4)

# # После вывожу все гипотезы предварительно обрезав предложения с помощью регулярки
# cv_sample = re.sub(r'([\.!?])[^\.!?]*$', r'\1', result)



# 11,,Junior Sales Manager,Junior,Sales,
# 12,,Middle Sales Manager,Middle,Sales,
# 13,,Senior Sales Manager,Senior,Sales,

# 16,Nielsen,Senior Product Manager,Senior,Product management,"Led product development, strategy and execution across four teams and launched five new products in three years, resulting in 25% revenue increase
# Led beta testing, data analytics and user research to identify and implement opportunities for improvement, leading to 80% increase in customer satisfaction
# Managed product team to build 7 mobile applications which helped the company retain upwards of $70k per month"
# 17,Dentons,Legal Assistant,Junior,Legal,"Conducted data gathering activities for 7 investigations regarding corporate law cases
# Managed confidential records and documents pertaining to litigation, divorce proceedings, and criminal negotiations
# Prepared 40+ legal agreements: commercial leases and merger agreements to ensure the terms comply with relevant regulations and are fair to the firm’s clients"
# 18,Booz Hamilton,Legal Consultant,Middle,Legal,"Represent 4 key clients at meetings of creditors and other proceedings related to their bankruptcy filings
# Counseled 28% of firm clients on legal options beyond a trial, increasing customer satisfaction scores by 33%
# Collaborated with 7 partners to conduct and consolidate legal research, increasing efficiency by 14%"
# 19,Optic,Senior Legal Consultant,Senior,Legal,"Developed case strategies in collaboration with clients, ensuring priorities were met while limiting financial strain, resulting in 84% positive feedback
# Defended 12 clients annually before a judge or jury, obtaining the desired case outcome 91% of the time"
# 20,Tinder,Customer Support Specialist,Junior,Customer Support,"Successfully resolved clients problems via messenger and phone with 80% Customer Satisfaction Score
# Effectively communicated with various departments (Sales,Technical etc) to meet the client's needs and solve their problems"
# 21,Badoo,Customer Support Manager,Middle,Customer Support,"Exceeded team’s annual goal of keeping client response rates above agreed SLAs (97%).
# Coordinated with the Sales and Product Departments in providing report analysis of trends in customer behavior and user experience every three months.
# Developed CRM tools tracking and reporting sales operations activities."
# 22,Figma,Customer Support Team Lead,Senior,Customer Support,"Reviewed and improved customer handling processes that accelerated case resolving by 22%
# Set KPI system for customer success team of 20+ members that improved satisfaction rate by 14%"
# 23,FromSoftware,Junior UX/UI Designer,Junior,UX/UI,"Created visual design prototypes, designed icons, and developed solutions for a new navigation system, resulting in a 10% increase in user satisfaction.
# Carried out user research through targeted interviews and extensive usability testing before and after redesign"
# 24,Naughty Dogs,UX/UI Designer,Middle,UX/UI,"Deployed new features with 13% higher performance than historical average
# Worked cross-functionally to deliver to 95% client satisfaction"
# 25,Platinum Games,UX/UI Desing Team Lead,Senior,UX/UI,"Created simple and intuitive user interfaces that contributed to 65% year on year profit growth.
# Collaborated with UX data analytics team and leveraged that data to create iterative improvements, increasing user satisfaction by 20%.
# Built SCRUM model to manage team of 12 UX designers that boosted task completion by 30%"
# 26,Uber,Junior HR Manager,Junior,HR,"Assisted in recruiting and onboarding of new employees for the marketing and IT teams
# Provided administrative support with payroll, calendars, meetings, and training events"
# 27,T-Mobile,HR Manager,Middle,HR,"Increased employee retention rates by managing workplace satisfaction to an over 90% success rate by creating and maintaining a positive work environment
# Developed plan to improve employee satisfaction that helped reduce employee turnover by 20%"
# 28,VMware,Senior HR Manager,Senior,HR,"Oversaw a human resources department of 16 team members and their various functions that improved managerial performance 23%
# Initiated and successfully managed two internship programs comprising 180 interns handling a budget of more than $350,000 incident-free"
# 29,AI21,Junior Data Scientist,Junior,Data Scientist,"Gathered and analyzed information relating to system security and cyber threat intelligence
# Used predictive analytics including data mining techniques to forecast company sales with 94% accuracy"
# 30,Webflow,Data Scientist,Middle,Data Scientist,"Built real-time ROI graphs that helped the teams focus on high-profit business increased 20% in annual profit.
# Created and presented models for potential holdings to fund managers that increased returns by 20% vs historical performance."
# 31,Figma,Data Science Team Lead,Senior,Data Scientist,"Led big data machine learning initiative that developed and deployed algorithms that allowed business to grow by 40%
# Developed model to accurately predict fraud activity, resulting in 75% decrease in company losses
# Managed a team of 8 data scientists and achieved 96% of backlog utility"
