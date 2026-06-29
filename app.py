import streamlit as st
import pandas as pd

from src.parser import load_candidates
from src.jd_processor import process_job_description
from src.final_ranker import hybrid_rank

st.set_page_config(
    page_title="Redrob Hybrid Candidate Ranking",
    layout="wide"
)

st.title("🚀 Redrob Hybrid Candidate Ranking System")

st.markdown("""
### Team NavaHanana

Hybrid candidate ranking pipeline using:

- Rule-based retrieval
- Honeypot detection
- Semantic reranking
- Explainable AI ranking
""")

jd_text = st.text_area(
    "Enter Job Description",
    """
Looking for Machine Learning Engineer
with 5 years experience in
Python, NLP, PyTorch,
Transformers, AWS and Docker.
""",
    height=180
)

if st.button("Run Candidate Ranking"):

    with st.spinner("Loading candidates..."):

        candidates = load_candidates(
            "data/sample_candidates.json"
        )

        candidates = candidates[:100]

    with st.spinner("Processing JD..."):

        jd = process_job_description(
            jd_text
        )

    with st.spinner("Ranking candidates..."):

        ranked = hybrid_rank(
            candidates,
            jd,
            jd_text
        )

    st.success(
        f"Ranked {len(candidates)} candidates"
    )

    rows = []

    for r in ranked[:10]:

        rows.append({
            "Candidate":
                r["candidate_id"],

            "Title":
                r["title"],

            "Score":
                round(
                    r["final_score"],
                    2
                )
        })

    st.subheader(
        "Top Candidates"
    )

    st.dataframe(
        pd.DataFrame(rows)
    )