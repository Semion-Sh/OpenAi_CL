request = {
    "Years of experience": "7",
    "Position that you apply for": "Senior Game Designer",
    "Company that you applied for": "Rovio",
    "Company where you worked previously": "VK Games",
    "Your last position at your last company where you worked": "Dame Designer",
    "Skills": "SQL, AB-tests, Python, MS Office, Excel, VBA, PowerPoint, Attention to details, Team management, Figma, Game Design"
}

hypotheses_intro = intro_generator.generate(create_prompt(request), num_hypos=5)
hypotheses_outro = outro_generator.generate(create_prompt(request), num_hypos=5)
hypotheses_wm = why_me_generator.generate(create_prompt(request), num_hypos=4, max_tokens=100)
hypotheses_exp = experience_generator.generate(create_prompt(request), num_hypos=4, max_tokens=100)
hypotheses_wc = why_company_generator.generate(create_prompt(request), num_hypos=4, max_tokens=90)

best_hypothesis_intro = ""
best_score = - 1
for hypothesis_intro in hypotheses_intro:
    quality_prompt_intro = create_prompt_quality(request, hypothesis_intro)
    score_intro = intro_classifier.classify(quality_prompt_intro)[0]
    if score_intro > best_score:
        best_score = score_intro
        best_hypothesis_intro = hypothesis_intro

best_hypothesis_wm = ""
best_score = - 1
for hypothesis_wm in hypotheses_wm:
    quality_prompt_wm = create_prompt_quality(request, hypothesis_wm)
    score_wm = why_me_classifier.classify(quality_prompt_wm)[0]
    if score_wm > best_score:
        best_score = score_wm
        best_hypothesis_wm = hypothesis_wm

total_pred = "\n\n".join(
    [best_hypothesis_intro, best_hypothesis_wm, best_hypothesis_exp, best_hypothesis_wc, best_hypothesis_outro])
total = re.sub(r'([\.!?])[^\.!?]*$', r'\1', total_pred)
print(total)
