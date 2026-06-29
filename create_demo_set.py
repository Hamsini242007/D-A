import json

from src.parser import load_candidates
from src.jd_processor import process_job_description
from src.ranker import rank_candidates

print("Loading 100000 candidates...")

candidates = load_candidates(
    "data/candidates.jsonl"
)

jd_text = """
Looking for Machine Learning Engineer
with 5 years experience
in Python, NLP, PyTorch,
Transformers, AWS and Docker.
"""

jd = process_job_description(
    jd_text
)

print("Running rule-based ranking...")

ranked = rank_candidates(
    candidates,
    jd
)

top250_ids = {
    c["candidate_id"]
    for c in ranked[:250]
}

demo_candidates = []

for candidate in candidates:
    if candidate["candidate_id"] in top250_ids:
        demo_candidates.append(candidate)

print(
    "Selected:",
    len(demo_candidates),
    "candidates"
)

with open(
    "data/demo_candidates.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        demo_candidates,
        f,
        indent=2
    )

print(
    "Saved:",
    "data/demo_candidates.json"
)