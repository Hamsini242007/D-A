# Redrob Intelligent Candidate Discovery & Ranking System

## Team

**Team Name:** NavaHanana

* **Hamsini Lalith Karkera** — Lead ML Engineer & System Design
* **Nithika Satheesha Mendon** — Data Engineering & Evaluation

---

## Problem Statement

Traditional candidate search systems rely heavily on keyword matching, resulting in poor candidate relevance, vulnerability to keyword stuffing, and inability to capture semantic similarity between candidate profiles and job descriptions.

The objective of this challenge is to identify and rank the top candidates from a pool of 100,000 candidate profiles while avoiding honeypots, behavioral traps, and profile inconsistencies.

---

## Solution Overview

We developed a hybrid candidate ranking pipeline that combines:

* Rule-based candidate retrieval
* Behavioral signal analysis
* Honeypot detection
* Retrieval-based candidate filtering
* Semantic reranking
* Explainable ranking generation

The system first narrows the candidate pool using explicit candidate-job matching signals and then performs semantic reranking on the retrieved candidate subset.

---

## Production Architecture

```text
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
```

---

## Key Features

### Hybrid Ranking

Combines symbolic matching and semantic similarity scoring.

### Behavioral Signal Analysis

Utilizes recruiter engagement signals and profile quality indicators.

### Honeypot Detection

Detects profile inconsistencies using:

* Experience mismatch checks
* Invalid salary ranges
* Behavioral anomalies
* Activity timeline inconsistencies

### Semantic Reranking

Uses SentenceTransformer embeddings to identify candidates with strong contextual similarity to the target job description.

### Explainable Ranking

Generates human-readable explanations for candidate rankings.

---

## Methodology

### Stage 1: Candidate Scoring

Candidates are scored using:

* Skill overlap
* Role similarity
* Experience alignment
* Recruiter engagement metrics
* Profile completeness
* Career progression

### Stage 2: Honeypot Detection

Candidate profiles are evaluated for:

* Experience inconsistencies
* Salary anomalies
* Invalid activity timelines
* Behavioral irregularities

### Stage 3: Retrieval

The highest scoring candidates are selected to form a retrieval pool of approximately 250 candidates.

### Stage 4: Semantic Reranking

The retrieval pool is reranked using SentenceTransformer semantic similarity between:

* Candidate profile representations
* Target job description representation

### Stage 5: Final Ranking

Final candidate scores are generated using a weighted hybrid scoring framework.

---

## Results

| Metric                | Result         |
| --------------------- | -------------- |
| Candidate Pool        | 100,000        |
| Retrieved Candidates  | 250            |
| Final Submission Size | 100            |
| Runtime               | 110.74 seconds |
| Hardware              | CPU Only       |
| Honeypot Rate         | 0%             |
| Top-100 Honeypots     | 0              |

Top candidate analysis demonstrated strong alignment with AI and Machine Learning roles while successfully excluding all detected honeypot candidates from the final top-100 ranking.

---

## Repository Structure

```text
.
├── data
├── docs
├── notebooks
│   └── analysis.ipynb
├── outputs
│   └── team_submission.csv
├── src
├── app.py
├── create_demo_set.py
├── test_hybrid.py
├── README.md
├── requirements.txt
├── submission_metadata.yaml
├── validate_submission.py
└── .gitignore
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Reproducing Results

Generate the final submission:

```bash
python -m src.submission
```

Validate the submission:

```bash
python validate_submission.py outputs/team_submission.csv
# Expected output: Submission is valid.
```

Analyze the final top-100:

```bash
python -m src.analyze_top100
```

Check honeypot rate:

```bash
python -m src.check_top100
```

---

## Interactive Sandbox

Streamlit Demo:
https://y4pmxssvbu93ejojxtngvu.streamlit.app/

The sandbox demonstrates the retrieval and semantic reranking pipeline on a representative candidate subset derived from the original 100,000 candidate dataset.

---

## Repository

GitHub Repository:

https://github.com/Hamsini242007/D-A

## Technologies Used

* Python
* SentenceTransformers
* HuggingFace Transformers
* PyTorch
* Scikit-Learn
* Streamlit
* Pandas
* NumPy

---

## Declaration

This project was developed as part of the Redrob Intelligent Candidate Discovery & Ranking Challenge. AI tools were used for engineering assistance, debugging, and documentation support. Final implementation decisions, experimentation, validation, and system design were performed by the team.
