from src.parser import load_candidates

candidates = load_candidates(
    "data/candidates.jsonl"
)

print(
    candidates[0]["redrob_signals"].keys()
)

for k in candidates[0]["redrob_signals"]:
    print(k)