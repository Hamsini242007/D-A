# Final Architecture — Redrob Intelligent Candidate Discovery & Ranking System

## Overview

The proposed solution implements a hybrid candidate ranking architecture designed to identify the most suitable candidates from a pool of 100,000 candidate profiles while minimizing the impact of keyword stuffing, behavioral anomalies, and honeypot profiles.

The architecture combines explicit rule-based retrieval, behavioral signal analysis, honeypot detection, and semantic reranking to generate the final top-100 candidate ranking.

---

## System Architecture

```text
100000 Candidate Profiles
            │
            ▼
──────────────────────────────
Stage 1: Candidate Parsing
──────────────────────────────
            │
            ▼
──────────────────────────────
Stage 2: Rule-Based Scoring
──────────────────────────────
• Skill overlap
• Role alignment
• Experience matching
• Career progression
• Recruiter engagement
• Profile quality
            │
            ▼
──────────────────────────────
Stage 3: Behavioral Analysis
──────────────────────────────
• Profile completeness
• Recruiter response signals
• Candidate activity patterns
• Behavioral consistency
            │
            ▼
──────────────────────────────
Stage 4: Honeypot Detection
──────────────────────────────
• Experience mismatch checks
• Salary inconsistency checks
• Invalid activity timelines
• Behavioral anomaly detection
            │
            ▼
──────────────────────────────
Stage 5: Candidate Retrieval
──────────────────────────────
Top 250 candidates selected
            │
            ▼
──────────────────────────────
Stage 6: Semantic Reranking
──────────────────────────────
SentenceTransformer similarity
between:
• Candidate profile
• Job description
            │
            ▼
──────────────────────────────
Stage 7: Hybrid Score Fusion
──────────────────────────────
Rule Score + Semantic Score
            │
            ▼
──────────────────────────────
Final Top-100 Ranking
──────────────────────────────
```

---

## Component Description

### 1. Candidate Parsing

The candidate dataset is loaded and parsed from the provided JSONL file containing 100,000 candidate profiles. Relevant profile information, behavioral signals, experience history, and skill data are extracted for downstream processing.

---

### 2. Rule-Based Candidate Scoring

Candidate profiles are initially scored using explicit matching criteria:

* Technical skill overlap
* Job title alignment
* Years of experience
* Career progression history
* Recruiter engagement indicators
* Profile completeness metrics

This stage generates an interpretable candidate relevance score.

---

### 3. Behavioral Signal Analysis

The system evaluates candidate behavioral attributes provided in the Redrob signal framework, including:

* Profile quality indicators
* Recruiter interaction signals
* Activity consistency
* Behavioral reliability measures

These signals improve candidate quality estimation beyond simple keyword matching.

---

### 4. Honeypot Detection

To reduce vulnerability to synthetic and misleading profiles, the system performs multiple consistency checks:

* Claimed experience versus actual career duration
* Salary range validation
* Account activity timeline validation
* Behavioral anomaly detection

Candidates exhibiting suspicious patterns receive penalties or are filtered from the final ranking.

---

### 5. Retrieval Stage

Rather than performing computationally expensive semantic ranking on all 100,000 candidates, the system first retrieves the top 250 candidates using rule-based scoring.

This retrieval stage significantly reduces computational cost while preserving candidate quality.

---

### 6. Semantic Reranking

The retrieved candidate pool is reranked using SentenceTransformer embeddings.

Semantic similarity is computed between:

* Candidate profile representations
* Target job description representations

This stage captures contextual similarity beyond exact keyword matching.

---

### 7. Hybrid Score Fusion

The final candidate ranking score is generated using a weighted combination of:

* Rule-based candidate score
* Semantic similarity score

This hybrid approach balances interpretability and semantic understanding.

---

## Performance

| Metric           | Value          |
| ---------------- | -------------- |
| Candidate Pool   | 100,000        |
| Retrieval Pool   | 250            |
| Final Submission | 100            |
| Runtime          | 110.74 seconds |
| Compute          | CPU Only       |
| Honeypot Rate    | 0%             |

---

## Design Decisions

The architecture was designed around four primary objectives:

1. Maintain interpretability through explicit scoring.
2. Improve candidate relevance using semantic representations.
3. Minimize computational cost using retrieval-based ranking.
4. Prevent ranking manipulation using behavioral and honeypot analysis.

The resulting system provides a scalable, explainable, and robust candidate ranking pipeline suitable for large-scale candidate discovery tasks.
