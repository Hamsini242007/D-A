# NavaHanana — Intelligent Candidate Discovery & Ranking System

## Overview

This project was developed for the **Redrob Hackathon: Intelligent Candidate Discovery & Ranking Challenge**.

We designed a hybrid candidate ranking pipeline that combines:

* Rule-based candidate retrieval
* Behavioral signal analysis
* Honeypot detection
* Semantic reranking using transformer embeddings
* Explainable candidate recommendations

The system processes **100,000 candidate profiles** and produces a ranked top-100 candidate list for a target job description while satisfying the challenge constraints:

* CPU-only execution
* No network access during ranking
* Runtime under 5 minutes
* Honeypot rate below 10%

---

## Problem Statement

Traditional resume ranking systems rely heavily on keyword matching, making them vulnerable to:

* Keyword stuffing
* Profile inconsistencies
* Behavioral anomalies
* Semantically relevant candidates being overlooked

Our objective was to build a robust candidate ranking system capable of:

* Understanding candidate-job semantic alignment
* Detecting suspicious candidate profiles
* Leveraging recruiter interaction signals
* Producing explainable rankings

---

## System Architecture

```text
Job Description
       |
       v
JD Processing
       |
       v
100K Candidate Pool
       |
       v
Rule-Based Retrieval
       |
       v
Behavioral Signal Scoring
       |
       v
Honeypot Detection
       |
       v
Top-250 Candidate Selection
       |
       v
SentenceTransformer Semantic Reranking
       |
       v
Hybrid Score Fusion
       |
       v
Explainability Layer
       |
       v
Final Top-100 Candidates
```

---

## Methodology

### 1. Job Description Processing

The job description is parsed to extract:

* Target role
* Required experience
* Required skills
* Technical keywords

Example:

```text
Machine Learning Engineer
5 years experience
Python
NLP
PyTorch
Transformers
AWS
Docker
```

---

### 2. Rule-Based Candidate Ranking

Candidates are scored using:

* Skill overlap
* Experience matching
* Title relevance
* Career trajectory
* Recruiter engagement signals
* Profile completeness

This stage retrieves the strongest candidates from the full pool of 100,000 candidates.

---

### 3. Honeypot Detection

The dataset contains intentionally deceptive profiles.

Our honeypot detection identifies:

* Experience inconsistencies
* Salary inconsistencies
* Behavioral anomalies
* Profile reliability issues

Results:

* Candidates analyzed: 100,000
* Honeypots detected: 24,925
* Honeypot rate in final Top-100: **0%**

---

### 4. Semantic Reranking

We use:

* SentenceTransformer
* Model: `all-MiniLM-L6-v2`

Candidate profiles and job descriptions are embedded into a shared semantic space.

The top 250 candidates from rule-based retrieval are reranked using cosine similarity.

---

### 5. Hybrid Ranking

Final ranking score:

```text
Final Score =
0.7 × Rule Score +
0.3 × Semantic Score
```

This combines:

* explicit skill matching
* behavioral evidence
* semantic understanding

---

### 6. Explainability

Each candidate includes a generated explanation describing:

* matched skills
* experience relevance
* recruiter engagement
* profile consistency

Example:

> Machine Learning Engineer with 7.1 years of experience demonstrates strong alignment through Python, NLP, PyTorch, and AWS skills. The candidate also shows healthy recruiter engagement with no detected profile inconsistencies.

---

## Results

### Runtime Performance

| Metric               | Value          |
| -------------------- | -------------- |
| Candidates processed | 100,000        |
| Execution mode       | CPU only       |
| Runtime              | 110.74 seconds |
| Memory               | 16 GB RAM      |

---

### Candidate Quality

| Metric                          | Value      |
| ------------------------------- | ---------- |
| Honeypot rate                   | 0%         |
| Average experience              | 4.93 years |
| Average recruiter response rate | 0.60       |

---

### Top Candidate Distribution

| Role                          | Count |
| ----------------------------- | ----- |
| AI Research Engineer          | 20    |
| ML Engineer                   | 19    |
| Junior ML Engineer            | 15    |
| Senior Software Engineer (ML) | 12    |
| AI Specialist                 | 11    |
| Machine Learning Engineer     | 10    |

---

## Repository Structure

```text
indiaruns-ai-ranking/

├── data/
│   ├── candidate_schema.json
│   ├── sample_candidates.json
│   ├── sample_submission.csv
│   └── submission_metadata_template.yaml
│
├── docs/
│   ├── final_architecture.md
│   ├── job_description.docx
│   ├── README.docx
│   ├── redrob_signals_doc.docx
│   └── submission_spec.docx
│
├── notebooks/
│   └── analysis.ipynb
│
├── outputs/
│   └── team_submission.csv
│
├── src/
│   ├── analyze_top100.py
│   ├── check_top100.py
│   ├── embeddings.py
│   ├── explain.py
│   ├── final_ranker.py
│   ├── honeypot.py
│   ├── jd_processor.py
│   ├── parser.py
│   ├── ranker.py
│   ├── scorer.py
│   ├── semantic_ranker.py
│   └── submission.py
│
├── .gitignore
├── README.md
├── requirements.txt
├── submission_metadata.yaml
└── validate_submission.py
```


---

## Reproducibility

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate the submission:

```bash
python src/submission.py
```

Validate:

```bash
python validate_submission.py outputs/team_submission.csv
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* SentenceTransformers
* HuggingFace Transformers
* PyTorch
* Scikit-Learn

---

## Team

### Team NavaHanana

* Hamsini Lalith Karkera — Team Lead / ML Engineer
* Nithika Satheesha Mendon — Data Analysis & Evaluation

---

## Challenge Compliance

* ✓ CPU-only execution
* ✓ No external API calls during ranking
* ✓ Runtime under 5 minutes
* ✓ Explainable rankings
* ✓ Honeypot detection
* ✓ Reproducible pipeline
* ✓ Valid submission format
