from honeypot import detect_honeypots


def score_candidate(candidate, job):

    score = 0

    # -------- Skill Match --------

    skill_weights = {
        "python": 10,
        "pytorch": 10,
        "nlp": 10,
        "transformers": 10,
        "llm": 10,
        "fine-tuning": 10,
    
        "docker": 3,
        "aws": 3,
        "airflow": 2,
        "spark": 2
    }
    
    candidate_skills = {
        s["name"].lower()
        for s in candidate["skills"]
    }
    
    skill_score = 0
    
    for skill in job["skills"]:
    
        weight = skill_weights.get(
            skill.lower(),
            5
        )
    
        if skill.lower() in candidate_skills:
            skill_score += weight
    
    skill_score = min(skill_score, 35)
    
    score += skill_score

    # -------- Experience --------
    required_exp = job["experience"]

    candidate_exp = candidate["profile"][
        "years_of_experience"
    ]

    if required_exp is not None:
        diff = abs(
            candidate_exp -
            required_exp
        )

        exp_score = max(
            0,
            20 - diff * 2
        )
    else:
        exp_score = 10

    score += exp_score

    # -------- Career Match --------

    candidate_title = (
        candidate["profile"]
        ["current_title"]
        .lower()
    )
    
    career_score = -10
    
    if job["role"]:
    
        if job["role"] in candidate_title:
            career_score = 15
    
        elif (
            "machine learning" in job["role"]
            and (
                "ml" in candidate_title
                or "ai" in candidate_title
                or "ai research" in candidate_title
            )
        ):
            career_score = 12
    
        elif (
            "data scientist" in candidate_title
            or "data engineer" in candidate_title
        ):
            career_score = 8

        elif (
            "software engineer" in candidate_title
            or "backend engineer" in candidate_title
        ):
            career_score = 5
        elif (
            "devops" in candidate_title
            or "qa" in candidate_title
            or ".net" in candidate_title
            or "cloud" in candidate_title
        ):
            career_score = -10
    
    score += career_score
    
    # -------- Behavioral --------
    signals = candidate["redrob_signals"]

    behavioral = (
        signals["profile_completeness_score"]
        / 100
    ) * 10

    score += behavioral

    # -------- Honeypots --------
    hp = detect_honeypots(candidate)

    score -= hp["honeypot_score"]

    return {
        "score": round(score, 2),
        "honeypots": hp["issues"]
    }


if __name__ == "__main__":

    from parser import load_candidates
    from jd_processor import process_job_description

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    jd = process_job_description(
        """
        Looking for Machine Learning
        Engineer with 5 years experience
        in Python, NLP, PyTorch,
        Transformers, AWS and Docker.
        """
    )

    result = score_candidate(
        candidates[0],
        jd
    )

    print(result)