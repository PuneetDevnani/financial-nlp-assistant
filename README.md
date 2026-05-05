# 💼 Financial NLP Assistant


## 🚀 Overview

Financial NLP Assistant is a BloombergGPT-inspired AI system designed to analyze and understand financial text using state-of-the-art NLP models.

The system integrates multiple domain-specific models to perform:

- 📊 Financial Sentiment Analysis (FinBERT)
- 📝 Financial Text Summarization (PEGASUS)
- ❓ Context-Aware Financial Question Answering (FLAN-T5)
- 🔁 Reproducibility & Data Integrity Validation
- 📂 Batch Processing with CSV Export
- 🌐 Interactive Web UI using Gradio

Unlike generic NLP pipelines, this system is tailored specifically for financial data, enabling more accurate insights from earnings reports, news articles, and market commentary.

---

## 🎯 Problem Statement

Financial text is complex, noisy, and context-heavy. Traditional NLP models struggle with:

- Domain-specific sentiment understanding  
- Long-form financial document summarization  
- Context-bound reasoning for question answering  
- Consistent and reproducible outputs  

This project addresses these challenges by building a modular financial NLP pipeline inspired by BloombergGPT using open-source models.

---

## 🧠 Key Highlights

- End-to-end financial NLP pipeline
- Multi-model architecture (FinBERT + PEGASUS + FLAN-T5)
- Data cleaning (noise removal, deduplication)
- Drift detection using embeddings
- Deterministic outputs via seed fixing
- Interactive UI + batch processing support
- Structured output generation (CSV + JSON)

---

## 🏗️ System Architecture

The pipeline follows a structured flow:

1. Input (Text + Optional Question)
2. Data Integrity Checks (noise removal, deduplication)
3. Sentiment Analysis
4. Financial Summarization
5. Question Answering
6. Reproducibility Validation
7. Output Export (CSV + JSON)

---

## 📊 Results

The system was tested on real-world financial text samples and successfully produced:

- Accurate sentiment classification with confidence scores  
- Concise and relevant financial summaries  
- Context-aware answers to financial queries  
- Stable outputs across multiple runs  

---

## ⚠️ Disclaimer

This project is an academic implementation inspired by BloombergGPT and does not use proprietary datasets or models.
