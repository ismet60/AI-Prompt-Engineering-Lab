# Lab 07 — Hands-on Sentiment Analysis with Python

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![TextBlob](https://img.shields.io/badge/TextBlob-Sentiment%20Analysis-1D9E75)
![Level](https://img.shields.io/badge/Level-Foundational-1D9E75)

Analyze sample customer feedback using TextBlob to explore sentiment polarity and subjectivity.

## What You Will Learn

- Import TextBlob and create a text object.
- Interpret polarity from -1 (negative) to 1 (positive).
- Examine subjectivity from 0 (objective) to 1 (subjective).
- Apply polarity scoring to several business feedback comments.

## Prerequisites

Install Python and [uv](https://docs.astral.sh/uv/). From this lab folder, run:

```powershell
uv sync
uv run python sentiment_analysis.py
```

The first setup requires internet access to install dependencies. The output shows the sample text, its polarity and subjectivity, and a polarity score for each feedback comment.

## Tasks

1. Import TextBlob and display a sample message.
2. Analyze the sentiment of a product review.
3. Score a list of business feedback comments.

## Takeaway

Sentiment scores help summarize feedback, but automated results may miss context, sarcasm, or mixed opinions. Review results before making business decisions.

## Screenshots

![TextBlob installation](screenshots/01-textblob-installation.png)

![Importing TextBlob](screenshots/02-import-textblob.png)

![Sentiment analysis result](screenshots/03-sentiment-analysis.png)

![Customer feedback results](screenshots/04-customer-feedback.png)
