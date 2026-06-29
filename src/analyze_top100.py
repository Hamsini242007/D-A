from collections import Counter

from src.parser import load_candidates
from src.jd_processor import process_job_description
from src.final_ranker import hybrid_rank


candidates = load_candidates(
    "data/candidates.jsonl"
)

lookup = {
    c["candidate_id"]: c
    for c in candidates
}

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

titles = []
experience = []
response_rates = []

for r in top100:

    c = lookup[
        r["candidate_id"]
    ]

    titles.append(
        c["profile"][
            "current_title"
        ]
    )

    experience.append(
        c["profile"][
            "years_of_experience"
        ]
    )

    response_rates.append(
        c["redrob_signals"][
            "recruiter_response_rate"
        ]
    )

print("\nTOP TITLES\n")

for title, count in Counter(
        titles
    ).most_common(20):

    print(
        title,
        ":",
        count
    )

print("\nAVERAGE EXPERIENCE")

print(
    round(
        sum(experience) /
        len(experience),
        2
    )
)

print("\nAVERAGE RESPONSE RATE")

print(
    round(
        sum(response_rates) /
        len(response_rates),
        2
    )
)