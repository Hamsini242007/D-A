import json
import time
import streamlit as st

from src.jd_processor import process_job_description
from src.final_ranker import hybrid_rank


st.set_page_config(
    page_title="Redrob AI Candidate Ranker",
    layout="wide"
)

st.title("Redrob AI Candidate Discovery & Ranking")
st.caption(
    "Hybrid Retrieval + Semantic Reranking System"
)

# load demo candidates
@st.cache_data
def load_demo():
    with open(
        "data/demo_candidates.json",
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)

candidates = load_demo()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Original Candidate Pool",
    "100,000"
)

col2.metric(
    "Retrieved Pool",
    "250"
)

col3.metric(
    "Ranking Method",
    "Hybrid"
)

st.success(
    f"Loaded {len(candidates)} retrieved candidates "
    "(from original 100,000 candidate pool)"
)

jd_text = st.text_area(
    "Job Description",
    value="""
Looking for Machine Learning Engineer
with 5 years experience
in Python, NLP, PyTorch,
Transformers, AWS and Docker.
""",
    height=200
)

if st.button("Run Hybrid Ranking"):

    start = time.time()

    jd = process_job_description(
        jd_text
    )

    results = hybrid_rank(
        candidates,
        jd,
        jd_text
    )

    runtime = (
        time.time() - start
    )

    st.subheader(
        "Top Candidates"
    )

    for i, c in enumerate(
        results[:10],
        start=1
    ):

        with st.expander(
            f"#{i} — "
            f"{c['name']} "
            f"({c['title']})"
        ):

            candidate = next(
                x for x in candidates
                if x["candidate_id"]
                == c["candidate_id"]
            )

            st.write(
                "Candidate ID:",
                c["candidate_id"]
            )

            st.write(
                "Experience:",
                candidate["profile"][
                    "years_of_experience"
                ],
                "years"
            )

            skills = [
                s["name"]
                for s in candidate["skills"][:8]
            ]

            st.write(
                "Skills:",
                ", ".join(skills)
            )

            st.write(
                "Rule Score:",
                round(
                    c["rule_score"],
                    2
                )
            )

            st.write(
                "Semantic Score:",
                round(
                    c["semantic_score"],
                    4
                )
            )

            st.write(
                "Final Score:",
                round(
                    c["final_score"],
                    2
                )
            )

    st.success(
        f"Completed in "
        f"{runtime:.2f} seconds"
    )

st.markdown("---")
st.subheader("Production Architecture")
st.code(
    """
100000 Candidates
       ↓
Rule-Based Retrieval
       ↓
Behavioral Signal Analysis
       ↓
Honeypot Detection
       ↓
Top-250 Candidate Retrieval
       ↓
Semantic Reranking
       ↓
Final Top-100 Submission
""",
    language="text",
)
st.write(
    "This sandbox demonstrates the semantic reranking "
    "stage using the retrieved candidate pool generated "
    "from the original 100000 candidate dataset."
)
