from src.parser import load_candidates
from src.jd_processor import process_job_description
from src.scorer import score_candidate


def rank_candidates(candidates, job):

    ranked = []

    for candidate in candidates:

        result = score_candidate(
            candidate,
            job
        )

        ranked.append({
            "candidate_id":
                candidate["candidate_id"],

            "name":
                candidate["profile"][
                    "anonymized_name"
                ],

            "title":
                candidate["profile"][
                    "current_title"
                ],

            "score":
                result["score"],

            "honeypots":
                result["honeypots"]
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked


if __name__ == "__main__":

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

    rankings = rank_candidates(
        candidates,
        jd
    )

    print("\nTOP 10\n")

    for r in rankings[:10]:
        print(r)



def rank_candidates(candidates, job):

    ranked = []

    for candidate in candidates:

        result = score_candidate(
            candidate,
            job
        )

        ranked.append({
            "candidate_id":
                candidate["candidate_id"],

            "name":
                candidate["profile"][
                    "anonymized_name"
                ],

            "title":
                candidate["profile"][
                    "current_title"
                ],

            "score":
                result["score"],

            "honeypots":
                result["honeypots"]
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked


if __name__ == "__main__":

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

    rankings = rank_candidates(
        candidates,
        jd
    )

    print("\nTOP 10\n")

    for r in rankings[:10]:
        print(r)
    print("\n\nTOP CANDIDATE DETAILS\n")
    
    top = rankings[0]
    
    candidate = None
    
    for c in candidates:
        if c["candidate_id"] == top["candidate_id"]:
            candidate = c
            break
    
    print("ID:", candidate["candidate_id"])
    print("TITLE:", candidate["profile"]["current_title"])
    print("HEADLINE:", candidate["profile"]["headline"])
    print("EXPERIENCE:", candidate["profile"]["years_of_experience"])
    
    print("\nSKILLS:")
    for s in candidate["skills"]:
        print("-", s["name"])
    
    print("\nCAREER:")
    for job in candidate["career_history"]:
        print(job["title"], "-", job["company"])
    
    print("\n\nSECOND CANDIDATE DETAILS\n")

    top = rankings[1]
    
    candidate = None
    
    for c in candidates:
        if c["candidate_id"] == top["candidate_id"]:
            candidate = c
            break
    
    print("ID:", candidate["candidate_id"])
    print("TITLE:", candidate["profile"]["current_title"])
    print("HEADLINE:", candidate["profile"]["headline"])
    print("EXPERIENCE:", candidate["profile"]["years_of_experience"])
    
    print("\nSKILLS:")
    for s in candidate["skills"]:
        print("-", s["name"])
    
    print("\nCAREER:")
    for job in candidate["career_history"]:
        print(job["title"], "-", job["company"])