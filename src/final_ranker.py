from parser import load_candidates
from jd_processor import process_job_description
from ranker import rank_candidates
from embeddings import semantic_similarity


def hybrid_rank(candidates, jd, jd_text):

    ranked = rank_candidates(
        candidates,
        jd
    )

    top_candidates = ranked[:250]

    candidate_lookup = {
        c["candidate_id"]: c
        for c in candidates
    }

    final = []

    for c in top_candidates:

        candidate = candidate_lookup[
            c["candidate_id"]
        ]

        semantic = semantic_similarity(
            candidate,
            jd_text
        )

        final_score = (
            0.5 * c["score"]
            +
            0.5 * semantic * 100
        )

        final.append({

            "candidate_id":
                c["candidate_id"],

            "name":
                c["name"],

            "title":
                c["title"],

            "rule_score":
                c["score"],

            "semantic_score":
                round(semantic,4),

            "final_score":
                round(final_score,2)
        })

    final.sort(
        key=lambda x:
        x["final_score"],
        reverse=True
    )

    return final


if __name__ == "__main__":

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

    final = hybrid_rank(
        candidates,
        jd,
        jd_text
    )

    print("\nFINAL TOP 20\n")

    for x in final[:20]:
        print(x)