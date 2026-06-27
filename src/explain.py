def explain_candidate(candidate, job, score_result):

    reasons = []

    title = candidate["profile"]["current_title"]
    experience = candidate["profile"]["years_of_experience"]

    # Role alignment
    if job["role"]:
        if job["role"].lower() in title.lower():
            reasons.append(
                f"Strong role alignment: {title}"
            )

        elif (
            "ai" in title.lower()
            or "ml" in title.lower()
        ):
            reasons.append(
                f"Related AI/ML role experience: {title}"
            )

    # Skill match
    candidate_skills = {
        s["name"].lower()
        for s in candidate["skills"]
    }

    matched = []

    for skill in job["skills"]:
        if skill.lower() in candidate_skills:
            matched.append(skill)

    if matched:
        reasons.append(
            f"Matched {len(matched)} required skills: "
            + ", ".join(matched)
        )

    # Experience
    if job["experience"]:
        diff = abs(
            experience -
            job["experience"]
        )

        if diff <= 2:
            reasons.append(
                f"Experience closely matches requirement "
                f"({experience} years)"
            )

    # Career progression
    career = candidate["career_history"]

    if len(career) >= 2:
        reasons.append(
            f"Relevant career progression across "
            f"{len(career)} roles"
        )

    # Behavioral signals
    signals = candidate["redrob_signals"]

    if signals["profile_completeness_score"] > 80:
        reasons.append(
            "High profile completeness"
        )

    # Honeypots
    if len(score_result["honeypots"]) == 0:
        reasons.append(
            "No profile inconsistencies detected"
        )
    else:
        reasons.append(
            "Detected issues: "
            + ", ".join(
                score_result["honeypots"]
            )
        )

    return reasons


if __name__ == "__main__":

    from parser import load_candidates
    from jd_processor import process_job_description
    from scorer import score_candidate

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

    candidate = candidates[30030]

    result = score_candidate(
        candidate,
        jd
    )

    explanation = explain_candidate(
        candidate,
        jd,
        result
    )

    print(candidate["candidate_id"])
    print()

    for r in explanation:
        print("-", r)