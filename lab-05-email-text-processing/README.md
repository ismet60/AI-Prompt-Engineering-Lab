# Lab 05 — Hands-on Text Processing for Email Management

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-Text%20Processing-1D9E75?style=flat-square)
![uv](https://img.shields.io/badge/Package%20Manager-uv-6F42C1?style=flat-square)
![Level](https://img.shields.io/badge/Level-Foundational-1D9E75?style=flat-square)

Process sample business emails with NLTK, compare stemming and lemmatization, and explore a simple keyword-based email categorizer.

---

## What You Will Learn

| Skill | Purpose |
| --- | --- |
| Tokenization | Split an email into words and punctuation. |
| Stemming | Reduce words to stems using PorterStemmer. |
| Lemmatization | Use WordNet and part-of-speech tags to find base forms. |
| Comparison | Examine differences between the two techniques. |
| Email categorization | Match keywords to simple business categories. |

## Prerequisites

- Python 3.10 or later
- Python packages: NLTK (`nltk>=3.9,<4`)
- [uv](https://docs.astral.sh/uv/)
- Internet access for initial dependency and NLTK data downloads

## Setup and Run

Open a terminal in this lab folder and run:

```powershell
uv sync
uv run python email_processing.py
```

**Expected result:** The program displays the NLTK version, processes two sample emails, compares word forms, and categorizes sample messages. NLTK resources are downloaded or checked on the first run.

## Task 1 — Import Libraries

Import NLTK, PorterStemmer, and WordNetLemmatizer. The program prints the installed NLTK version to confirm that the library is available.

## Task 2 — Apply Stemming

Tokenize an email about project deadlines and apply PorterStemmer to each token. Stemming reduces words to stems, which may not be complete words: for example, `deadlines` becomes `deadlin`.

## Task 3 — Apply Lemmatization

Use WordNet to process a second email about team members and tasks. Part-of-speech tags help the lemmatizer identify a word's grammatical role; for example, `working` can become `work`.

## Compare the Results

The program compares stems, default noun lemmas, and POS-aware lemmas for the same email:

| Original | Stem | Default lemma | POS-aware lemma |
| --- | --- | --- | --- |
| working | work | working | work |
| submitted | submit | submitted | submit |
| promptly | promptli | promptly | promptly |

Stemming can produce non-words; lemmatization uses vocabulary and grammatical information, but predictions still need review in context.

## Bonus — Categorize Sample Emails

A simple keyword matcher assigns a sample message to **billing**, **technical issues**, **customer support**, or **general inquiry**. It is a basic demonstration: results depend on the keywords, and ties follow the category order in the code.

## Project Files

| File | Purpose |
| --- | --- |
| `email_processing.py` | Runs the lab tasks, comparison, and categorization. |
| `pyproject.toml` | Lists Python and NLTK requirements. |
| `uv.lock` | Records the resolved dependency versions. |

[← Back to all labs](../README.md)

