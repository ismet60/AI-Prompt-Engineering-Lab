# Lab 05 — Hands-on Text Processing for Email Management

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-Text%20Processing-1D9E75?style=flat-square)
![uv](https://img.shields.io/badge/Package%20Manager-uv-6F42C1?style=flat-square)
![Level](https://img.shields.io/badge/Level-Foundational-1D9E75?style=flat-square)

Normalize a sample business email with stemming and lemmatization, then compare the two approaches on the same text.

---

## What You Will Learn

| Skill | Purpose |
| --- | --- |
| Tokenization | Split an email into words and punctuation. |
| Stemming | Reduce words to stems using PorterStemmer. |
| Lemmatization | Use WordNet and part-of-speech tags to find base forms. |
| Comparison | Examine how the two methods change each token. |

## Prerequisites

- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/)
- Internet access for initial dependency and NLTK data downloads

## Setup and Run

Open Git Bash in this lab folder and run:

```bash
uv sync
uv run python email_processing.py
```

The first run downloads NLTK's tokenizer, English tagger, WordNet, and multilingual WordNet data. The program prints the original email, stemmed text, lemmatized text, and a token-by-token comparison.

## Tasks

1. **Import the libraries:** Load NLTK, PorterStemmer, and WordNetLemmatizer.
2. **Stem the email:** Reduce tokens to stems, which may not be complete words.
3. **Lemmatize the email:** Use POS tags to select the grammatical role for WordNet. For example, a verb tag can help reduce `working` to `work`.
4. **Compare the output:** Review both methods on the same email. Stemming is a fast rule-based reduction; lemmatization uses vocabulary and grammatical information, though its results depend on tagging accuracy.

## Project Files

| File | Purpose |
| --- | --- |
| `email_processing.py` | Runs the email normalization and comparison. |
| `pyproject.toml` | Lists Python and NLTK requirements. |
| `uv.lock` | Records the resolved dependency versions. |

[← Back to all labs](../README.md)
