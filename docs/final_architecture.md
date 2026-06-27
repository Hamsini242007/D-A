Stage 1:
Rule-based retrieval using:
- Skill match
- Experience match
- Career match
- Behavioral signals
- Honeypot detection

Stage 2:
Semantic reranking using
SentenceTransformer (all-MiniLM-L6-v2)

Stage 3:
Hybrid scoring:
Final Score =
0.5 × Rule Score +
0.5 × Semantic Score

Stage 4:
Explainability engine