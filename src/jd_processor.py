import re


SKILLS = {
    "python", "java", "sql", "aws", "gcp", "azure",
    "docker", "kubernetes", "spark", "airflow",
    "pytorch", "tensorflow", "nlp", "llm",
    "transformers", "fine-tuning", "lora",
    "rag", "langchain", "flask", "fastapi",
    "react", "node", "mongodb", "postgresql"
}


def process_job_description(job_description):

    text = job_description.lower()

    # experience extraction
    exp_match = re.search(r'(\d+)\+?\s*years', text)
    experience = int(exp_match.group(1)) if exp_match else None

    # skills extraction
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    # role extraction
    role = None

    role_keywords = [
    "machine learning engineer",
    "ml engineer",
    "ai engineer",
    "ai research engineer",
    "data scientist",
    "data engineer",
    "software engineer",
    "backend engineer",
    "frontend engineer",
    "full stack developer",
    "devops engineer",
    "cloud engineer"
    ]

    for r in role_keywords:
        if r in text:
            role = r
            break

    return {
        "role": role,
        "experience": experience,
        "skills": found_skills
    }


if __name__ == "__main__":

    jd = """
    Looking for a Machine Learning Engineer
    with 5+ years experience in Python,
    PyTorch, NLP, Transformers,
    LLM fine-tuning, AWS and Docker.
    """

    result = process_job_description(jd)

    print(result)