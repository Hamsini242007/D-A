def detect_honeypots(candidate):

    penalties = []
    score = 0

    signals = candidate["redrob_signals"]

    # Rule 1: Invalid salary range
    salary = signals["expected_salary_range_inr_lpa"]

    if salary["min"] > salary["max"]:
        penalties.append("invalid_salary_range")
        score += 50

    # Rule 2: Invalid dates
    if signals["signup_date"] > signals["last_active_date"]:
        penalties.append("invalid_activity_dates")
        score += 50

    # Rule 3: Experience mismatch
    claimed = candidate["profile"]["years_of_experience"]

    actual = (
        sum(
            job["duration_months"]
            for job in candidate["career_history"]
        ) / 12
    )

    if abs(claimed - actual) > 5:
        penalties.append("experience_mismatch")
        score += 75

    return {
        "honeypot_score": score,
        "issues": penalties
    }


if __name__ == "__main__":

    from parser import load_candidates

    candidates = load_candidates("data/candidates.jsonl")

    result = detect_honeypots(candidates[3429])

    print(candidates[3429]["candidate_id"])
    print(result)