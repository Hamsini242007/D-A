from embeddings import semantic_similarity
from ranker import rank_candidates
from parser import load_candidates
from jd_processor import process_job_description


if __name__ == "__main__":

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    jd_text = """
    Looking for Machine Learning Engineer
    with 5 years experience in
    Python, NLP, PyTorch,
    Transformers, AWS and Docker.
    """

    jd = process_job_description(
        jd_text
    )

    ranked = rank_candidates(
        candidates,
        jd
    )

    top_candidates = ranked[:100]

    semantic_results = []

    candidate_lookup = {
        c["candidate_id"]: c
        for c in candidates
    }

    for c in top_candidates:

        candidate = candidate_lookup[
            c["candidate_id"]
        ]

        score = semantic_similarity(
            candidate,
            jd_text
        )

        semantic_results.append({
            "candidate_id":
                c["candidate_id"],

            "name":
                c["name"],

            "title":
                c["title"],

            "semantic_score":
                score
        })

    semantic_results.sort(
        key=lambda x:
        x["semantic_score"],
        reverse=True
    )

    print("\nTOP 10 SEMANTIC\n")

    for x in semantic_results[:10]:
        print(x)