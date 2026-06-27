import json
from pathlib import Path
from tqdm import tqdm


def load_candidates(path):
    candidates = []

    with open(path, "r", encoding="utf-8") as f:
        for line in tqdm(f):
            candidates.append(json.loads(line))

    return candidates


if __name__ == "__main__":
    DATA_PATH = Path("data/candidates.jsonl")
    if not DATA_PATH.exists():
        DATA_PATH = Path("../data/candidates.jsonl")

    candidates = load_candidates(DATA_PATH)

    print(f"Loaded {len(candidates):,} candidates")
    print(candidates[0]["candidate_id"])