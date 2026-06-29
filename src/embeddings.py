from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_candidate_text(candidate):

    text = []

    profile = candidate["profile"]

    text.append(
        profile["current_title"]
    )

    text.append(
        profile["headline"]
    )

    text.append(
        profile["summary"]
    )

    for skill in candidate["skills"]:
        text.append(skill["name"])

    for job in candidate["career_history"]:
        text.append(job["title"])

        if job["description"]:
            text.append(
                job["description"]
            )

    return " ".join(text)


def semantic_similarity(
        candidate,
        job_text):

    candidate_text = (
        create_candidate_text(
            candidate
        )
    )

    cand_emb = model.encode(
        candidate_text
    )

    job_emb = model.encode(
        job_text
    )

    score = cosine_similarity(
        [cand_emb],
        [job_emb]
    )[0][0]

    return float(score)


if __name__ == "__main__":

    from src.parser import load_candidates

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    score = semantic_similarity(
        candidates[30030],
        """
        Machine Learning Engineer
        Python NLP PyTorch
        Transformers LLM
        AWS Docker
        """
    )

    print(score)