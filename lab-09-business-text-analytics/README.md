# Lab 09 — Business Text Analytics with NLP Techniques

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-Text%20Analytics-1D9E75?style=flat-square)
![uv](https://img.shields.io/badge/Package%20Manager-uv-6F42C1?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)

Apply text preprocessing, stemming, lemmatization, named entity recognition, part-of-speech tagging, and sentiment scoring to the SBA 927 dataset.

---

## What You Will Learn

| Skill | Purpose |
| --- | --- |
| Preprocessing | Tokenize and normalize text and filter punctuation and stop words. |
| Stemming and lemmatization | Compare rule-based stems with WordNet base forms. |
| Named entity recognition | Identify and review possible names and categories. |
| POS tagging | Identify grammatical roles using original text. |
| Sentiment analysis | Examine VADER scores while checking the context and limitations. |

## Dataset

The [assignment dataset](https://drive.google.com/file/d/1eUyPiLMJZbJutUuI1R4lUgHjc0G-z8vq/view) contains 12 nonempty passages about *I, Robot*. These are film-related passages, not actual customer feedback; results must not be presented as measured customer satisfaction.

Download the dataset from the assignment link and save it as `SBA927.txt` in this folder. The dataset is not included in this repository.

## Prerequisites

- Python 3.10 or later and [uv](https://docs.astral.sh/uv/)
- NLTK (`nltk>=3.9,<4`) and NumPy (`numpy>=2.2.6`)
- Internet access for installation and initial NLTK resource downloads

## Setup and Run

Open a terminal in this lab folder:

```powershell
uv sync
uv run python business_text_analysis.py
```

The first run downloads NLTK resources. For each passage, the program prints the original text, processed tokens, stems, lemmas, POS tags, named entities, and a VADER sentiment label and compound score.

## Task 1 — Tokenization and Preprocessing

The program tokenizes each passage, converts alphabetic tokens to lowercase, and removes English stop words and punctuation. This helps compare terms but can discard context; sentiment and named-entity analysis use the original text.

## Task 2 — Stemming and Lemmatization

Porter stemming reduces words to stems, which may not be dictionary words. WordNet lemmatization uses its default noun setting in this exercise. In the sample run, `robots` became `robot` with both methods; `futuristic` became `futurist` with stemming and stayed `futuristic` with lemmatization.

## Task 3 — Named Entity Recognition

NLTK's pre-trained entity chunker identifies candidate entities. In the sample run, `Detective Del Spooner` was tagged `PERSON`, while `Robot` was also tagged `PERSON` incorrectly. Review entity labels rather than treating them as verified facts.

## Task 4 — Part-of-Speech Tagging

The POS tagger assigns grammatical labels to tokens in the original text. For example, in the sample run, `investigates` was tagged `VBZ` (a third-person singular present-tense verb).

## Task 5 — Sentiment Prompt

A prompt drafted for comparison is:

```text
Classify the following passage as positive, negative, neutral, or mixed.
Explain the evidence briefly and identify uncertainty: [insert passage].
```

This prompt has not yet been tested. A meaningful evaluation should compare model output with human judgments and record disagreements.

## Task 6 — Sentiment Results and Evaluation

VADER labeled 7 passages positive, 2 negative, and 3 neutral in the initial run using compound thresholds of 0.05 and -0.05. These are model classifications, not accuracy measurements: there are no human gold labels in the dataset. Narrative context, mixed sentiment, punctuation, and negation can affect results.

## Task 7 — Pre-trained Model Experiment

The analysis uses NLTK's pre-trained POS and named entity models and VADER's sentiment lexicon. A **separate pre-trained language-model experiment and comparison remain to be completed** before the assessment is finished.

## Project Files

| File | Purpose |
| --- | --- |
| `business_text_analysis.py` | Runs the NLTK analysis. |
| `pyproject.toml` | Defines Python and package requirements. |
| `SBA927.txt` | Assignment dataset, downloaded separately. |

[← Back to all labs](../README.md)
