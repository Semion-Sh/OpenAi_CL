import pandas as pd
import ttm
from main import archivment
# Вот сам датасет:
summary_prompt = pd.read_csv('data/Summary_Dataset_QA.csv')


def create_request_summary(params):
    return f'Company name, where you worked on your position: {params["Company name"]}\n' + \
        f'Your position at company where you worked: {params["Position"]}\n' + \
        f'How many years do you work in this industry: {params["Years of Experience"]}\n' + \
        f'Level of your last position: {params["Grade"]}\n' + \
        f'Industry, where you worked on your position: {params["Industry"]}\n' + \
        f'Achievements and duties that you had on yor position in company: {params["Achievements"]}\n' + \
        f'''Generate a winning description of the experience of the person for a resume,
        incorporating years of experience, level of the position, position, company and industry: {params["Summary"]}\n'''


# После

summary_cv = []
for _, row in summary_prompt.iterrows():
    if row.iloc[1:].isna().all():
        continue
    sample = create_request_summary(row)
    summary_cv.append(sample)


# Затем реквест + джойн

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
# print(summary_fewshot)

# generated_summary_1 = ttm.generate(summary_fewshot, max_tokens=100)
# print(generated_summary_1)


# 20,DICE,3D Artist,2,Middle,Gaming,"Designed, modeled, and rigged different characters with 3Ds Max (V-Ray) and Maya
# Sketching and designing various elements within the game interface
# Together with a team of 7 other 3D artists worked on creating the storyboard for the game
# Participated in designing behind the various game areas - the design of the key tower was recognized by the Global Industry Game Awards (GIGA) under the 3D Environment Art category","Digital artist with professional background in 3d animations within the gaming industry. Passionate about creating unique, outside-this-world concepts with 3ds Max and Maya. Find my distinctive ""stamp"" in all of my designs - from objects and environments to characters.",1
# 21,HDR,Junior Architect,1,Junior,Architecture,"Created 2D drawings of floor plans, and sections using AutoCAD
# Used 3DS Max and VRay to render photorealistic visualizations for presentation and marketing purposes
# Assisted 5 Project Managers with reports, cost estimates, and timetables
# Performed research for the lead architect on specifications, materials, and building codes","Architect with over 1 year of experience in developing conceptual plans for commercial/residential buildings.
# Understanding of local building codes and ordinances, knowledgeable about requirements for public buildings and private residences. Worked with over 30 clients to create personal spaces that meet their needs.",1
# 22,Esquire,Event coordinator,4,Middle,Media,"Organized a gala dinner for approximately 1500 attendees
# Coordination of 60 educational events yearly for healthcare professionals
# Conducted volunteer and intern training and managed up to 40 event staff
# Project-led design & delivery of event features, including sales & registration areas for 3 years ensuring budget savings
# Hosted 30+ business events (up to 400 people): conferences, evening socials, filming sets, showcases, media events
# Organized a business event and acquired $90 000 in sponsorships",Event Coordinator with 4 years of experience in coordinating and executing large-scale events. Knowledgeable in developing budgets and managing staff. Meet deadlines and guarantee exceptional organization.,1
# 23,MIT,Teacher,6,Senior,Education,"Teaching classes of 25+ on biology and chemistry topics
# Participated in student recruitment, registration, and placement activities
# Contributed to raising retention rate from 75% - 89% through running extracurricular sessions
# Ran 100+ school information sessions","Conscientious and flexible High school teacher with 6 years of experience. Well-versed in using social skills and empathy to manage student behavior, utilize feedback from students to create compelling lesson plans that take into account the strengths and weaknesses of students. Looking to contribute my knowledge and skills to a school that offers a genuine opportunity for career progression.",1
# 24,HBO,Production assistant,1,Junior,Entertainment,"Edited news packages and interviews using Adobe Premier and Final Cut
# When there were studio live guests, increased team efficiency by 35% by overseeing the work of cameramen, lighting, and sound crew members
# Grew the studios' network by adding 4 new cameramen and a lighting crew to improve efficiency
# Assisted in making proposals for media, creating skeleton scripts for TV Stations","Production assistant with a 1-year track record of working on projects that boosted the media platform's profit by 20%. My portfolio of work includes over 80 pieces of film content for different platforms. Communicative, team player with a clear understanding of the filming process.",1
# 25,Council of the District of Columbia,Government Relations Specialist,3,Middle,Government Affairs,"Represented the issues in the current educational model at bi-weekly legislative sessions
# Lobbied for the state-wide rise in educational staffs' salaries by 25% and brought attention to the issue on a national level
# Created a social media campaign about salary inequalities in the educational sphere, raising awareness amongst the local community by 56%
# Worked on budget proposals to increase the annual ROI by 15%","Governemnt affairs Specialist with 3 years of experience a focus on ensuring national and state policies are thoroughly followed within the business. Establishing verification frameworks that are 100% accurate.  Manging teams and passionate about achieving equitable, future-facing causes. ",1
# 26,Zara,Sales Associate,5,Middle,Fashion,"Formulate and execute compelling seasonal sales promotions, resulting in over 30% increase in-store sales
# Proactively interact with customers to recommend products that best suit their tastes, interests, and needs, achieving o more than 98% in customer satisfaction rate
# Devised and implemented an effective sales process, leading to consistently achieving the established sales goals and surpassing the monthly sales target by 12%""
# Conceptualized and enforced a customer loyalty program that prompted both existing and new customers to purchase twice as much merchandise, resulting in a 50% increase in the department's sales","Growth-focused professional with 5+ years of dynamic sales experience across multiple industries. Equipped with a steadfast commitment to customer service excellence to enhance customer experience, maximize satisfaction, increase retention and business revenue. Possess superb abilities to develop and maintain o high level of product knowledge to persuasively promote them to existing and potential customers.",1
# 27,Amazon,Financial Analyst,1,Junior,E-commerce,"Maintained and monitored the fund and equity investments, including inflows, outflows, valuation, risk rating and performance analysis
# Prepared weekly reports and led presentations for the department director
# Reduced the material costs by 15% year-to-year","Financial analyst with 1 year of experience, specializing in informative and persuasive professional analytics and presentations. Bachelor's degree in finance and two related certifications from the Corporate finance Institute. Strong skills in financial modeling, budgeting, and forecasting, advanced Excel and SQL user.",1
# 28,Bank of America,Entry-Level Bank Teller,1,Junior,Finance,"Increased bank sales objectives by 20%
# Quickly established credibility with clients and remembered over 50+ names of regulars, creating a friendly rapport with customers
# Handled monthly business transactions, accounts payable, accounts receivable, and bank reconciliation of over 100 clients","Young specialist with 1 year of experience in the bank industry, maintained knowledge of bank products, services, and best practices. Provided customers with a high level of service, privacy, confidentiality, and a friendly, welcoming attitude. Handled all transactional services, including bank deposits, monetary withdrawals, financial transfers, and other bank transactions.",1
# 29,Merck & Co.,Data Analyst Intern,1,Junior,Pharmaceutical,"Performed checking data input or validate totals on forms prepared by others to detect errors in arithmetic, data entry, and procedures
# Introduced a new way of interpreting data to a team of 30 people
# Tested if all the forms were working and eliminated manual data collection process by 40%
# Processed over 1000 images, converting their per pixel spectral data into a dataset","Result-oriented data analyst with 1 year of experience. Strong knowledge in interpreting and analyzing data to drive growth for a pharmaceutical company. Skilled in finding insights, performing analytics, and business intelligence needed to guide decisions. Have practical experience using Excel (Advanced), SQL, Python, and Power BI.",1
# 30,Marriott,Receptionist,1,Junior,Hospitality,"Implemented processes to improve efficiency and customer service
# Scheduled 20+ appointments weekly and answered 60+ calls daily for questions and inquiries
# Ensured hotel guests feel comfortable by providing exceptional customer service
# Wrote 20+ emails daily and trained staff on communication and body language","Diligent Receptionist with 1 year of experience in the hospitality industry. Skilled in greeting and assisting clients, scheduling appointments, and answering phone calls and emails. Adept at working with databases, problem-solving, and coordinating activities. Exceptional communication skills and impressive body language.",1
# 16,Wrike,Senior IT Recruiter,6,Senior,IT,"Planned, organized and presented at national marketing events for 100+ international companies
# Worked in a team of 7 to recruit and source 200+ talents
# Organized and conducted on-campus recruiting, and ultimately made hiring decisions for 15 branch operators
# Recruited, trained, certified and led over 50 freelance photographers from the UK, Sweden and Denmark
# Conducted analysis and co-managed the annual budget of $381,500","Eclectic professional with 6 years of experience as an IT Recruiting Specialist. Skilled in searching and interviewing candidates, onboarding and training. Strong knowledge of various technologies and evaluating candidates' skills.",1
# 17,Admitad,Digital Marketing Specialist,4,Middle,Digital Marketing,"Tripled the company's mobile base to over 15k monthly active users
# Led Spotlime App from 0 to 125k app installs in 8 months
# Implemented Call-To-Action links, increasing click-through rates by 400% QoQ
# Organized a 350+ guests customer event for just a month
# 280+ blog articles published on digital channels","An experienced digital marketing specialist on a mission to boost sales and increase brand awareness. Professional in implementing SEO strategies for client websites including layout, content optimization, and keyword structuring. Proven understanding and implementation of pay-per-click, search engine optimization, google analytics, and data analysis.",1
# 18,PwC,Office Assistant,2,Middle,Consulting,"Planned and executed over 20 fundraisers, luncheons, and special events for groups of over 100 guests
# Reduced company expenditures by $18,000 in total by discovering billing errors
# Reduced electricity costs by 12% by suggesting solar upgrades
# Decreased paper wastage by 24% by introducing a “scan and email” method for filing receipts",A cheerful yet disciplined office assistant with over 2 years of experience in the field. Able to handle various administrative tasks at once. Excellent communicator and event planner.,1
# 19,EPAM,Scrum Master,7,Senior,Software Devlopement,"Delivered more than 50 projects with budgets from $50,000 to $1 million on-time and on-budget for clients such as Bank of New York and Arkema Corporation.
# Enabled the Agile team to increase its throughput by 15% through the use of swarming around features and other high-collaboration approaches, such as paired programming.
# Facilitated test-driven development on all projects increasing quality by 17% against historical data.
# Administered all Agile/Scrum processes including sprint planning, daily scrums, sprint reviews, and sprint retrospectives; coached team members and clients on Agile process.","Accomplished, committed, and creative Scrum Master with more than 7 years of success delivering IT projects on time and within budget through improved productivity, performance, and cost control. Broad experience leading and innovating in both Fortune 500 and boutique firm environments. Big 4 client-facing /client-management experience. Communicate effectively with all levels of management. Certified PMP and Scrum Master (PSM-l).",1
