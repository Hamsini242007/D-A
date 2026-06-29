from src.parser import load_candidates
from src.jd_processor import process_job_description
from src.final_ranker import hybrid_rank
from src.honeypot import detect_honeypots


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

lookup = {
    c["candidate_id"]: c
    for c in candidates
}

count = 0

for r in rankings[:100]:

    candidate = lookup[
        r["candidate_id"]
    ]

    result = detect_honeypots(
        candidate
    )

    if result["honeypot_score"] > 0:
        count += 1

print()
print(
    "Top100 honeypots:",
    count
)

print(
    "Rate:",
    round(count,2),
    "%"
)