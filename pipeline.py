import os
import random
import numpy as np
import torch
from transformers import pipeline

# -----------------------------
# REPRODUCIBILITY
# -----------------------------
SEED = 42
os.environ['PYTHONHASHSEED'] = str(SEED)
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

# -----------------------------
# LOAD MODELS
# -----------------------------
sent_pipe = pipeline("sentiment-analysis", model="yiyanghkust/finbert-tone")

sum_pipe = pipeline(
    "summarization",
    model="human-centered-summarization/financial-summarization-pegasus"
)

qa_pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

# -----------------------------
# FUNCTIONS
# -----------------------------
def finance_sentiment(text):
    res = sent_pipe(text)[0]
    return res["label"], float(res["score"])

def finance_summary(text):
    res = sum_pipe(text, max_length=120, min_length=40, do_sample=False)
    return res[0]["summary_text"]

def finance_qa(question, context):
    prompt = f"""
    Answer based only on context.
    Context: {context}
    Question: {question}
    Answer:
    """
    res = qa_pipe(prompt)
    return res[0]["generated_text"]

def bloomberg_pipeline(text, question=None):
    sentiment, score = finance_sentiment(text)
    summary = finance_summary(text)

    if question:
        answer = finance_qa(question, text)
    else:
        answer = "No question asked."

    return {
        "sentiment": sentiment,
        "confidence": round(score, 4),
        "summary": summary,
        "qa_answer": answer
    }