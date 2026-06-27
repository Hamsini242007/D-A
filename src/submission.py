import pandas as pd

from parser import load_candidates
from jd_processor import process_job_description
from final_ranker import hybrid_rank


candidates = load_candidates(
    "data/candidates.jsonl"
)

jd_text = """
Looking for Machine Learning Engineer
with 5 years experience in Python,
NLP, PyTorch, Transformers,
AWS and Docker.
"""

jd = process_job_description(
    jd_text
)

rankings = hybrid_rank(
    candidates,
    jd,
    jd_text
)

top100 = rankings[:100]
top100.sort(
    key=lambda x: (
        -x["final_score"],
        x["candidate_id"]
    )
)

max_score = top100[0]["final_score"]

submission = []

lookup = {
    c["candidate_id"]: c
    for c in candidates
}

for rank, r in enumerate(
        top100,
        start=1):

    candidate = lookup[
        r["candidate_id"]
    ]

    response_rate = (
        candidate[
            "redrob_signals"
        ][
            "recruiter_response_rate"
        ]
    )

    score = round(
        r["final_score"] /
        max_score,
        6
    )

    reasoning = (
        f"{r['title']} with "
        f"{candidate['profile']['years_of_experience']}"
        f" yrs; hybrid AI ranking "
        f"score {r['final_score']}; "
        f"response rate "
        f"{response_rate:.2f}."
    )

    submission.append({

        "candidate_id":
            r["candidate_id"],

        "rank":
            rank,

        "score":
            score,

        "reasoning":
            reasoning
    })

df = pd.DataFrame(
    submission
)

df.to_csv(
    "team_submission.csv",
    index=False
)

print(
    df.head()
)

print()
print(
    "Rows:",
    len(df)
)