from src.parser import load_candidates
from src.jd_processor import process_job_description
from src.final_ranker import hybrid_rank

print("Loading candidates...")

candidates = load_candidates(
    "data/candidates.jsonl"
)

print("Candidates loaded:", len(candidates))

jd_text = """
Looking for Machine Learning Engineer
with 5 years experience
in Python, NLP, PyTorch,
Transformers, AWS and Docker.
"""

print("Processing JD...")

jd = process_job_description(
    jd_text
)

print("Running hybrid ranker...")

result = hybrid_rank(
    candidates,
    jd,
    jd_text
)

print("\nTOP RESULT:\n")
print(result[0])

print("\nTOTAL RESULTS:")
print(len(result))