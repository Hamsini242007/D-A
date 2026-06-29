from src.embeddings import semantic_similarity
from src.ranker import rank_candidates
from src.parser import load_candidates
from src.jd_processor import process_job_description


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

    top_candidates = ranked[:250]

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

        rule_score = c["score"]

        final_score = (0.5 * rule_score+0.5 * (score * 100))

        semantic_results.append({
            "candidate_id":
                c["candidate_id"],

            "name":
                c["name"],

            "title":
                c["title"],

            "rule_score":
                rule_score,

            "semantic_score":
                round(score,4),

            "final_score":
                round(final_score,2)
        })

    semantic_results.sort(key=lambda x:x["final_score"],reverse=True)

    print("\nTOP 10 SEMANTIC\n")

    for x in semantic_results[:10]:
        print(x)