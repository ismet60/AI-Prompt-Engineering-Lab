# Lab 9 – Business Text Analytics: Natural Language Processing Techniques

## Description of the project
This project applies core NLP techniques to a small business-style text dataset, acting as a data analyst who extracts insight from text. The dataset (`business_text_data.txt`) has 12 lines of quotes and commentary about the film *I, Robot*.

| Requirement | What it does | Tools |
|---|---|---|
| 1. Tokenization and preprocessing | Tokenizes, lowercases, removes punctuation, numbers and stop words | NLTK |
| 2. Stemming and lemmatization | Compares Porter stemming with WordNet lemmatization | NLTK |
| 3. Named Entity Recognition (NER) | Finds people, organizations and places | NLTK |
| 4. Part-of-speech (POS) tagging | Labels the part of speech of every token | NLTK |
| 5–6. Sentiment prompt | A reusable prompt classifies business sentences as positive, negative or neutral and explains why | Groq model `openai/gpt-oss-20b` via LangChain |
| 7. Pre-trained models | Runs the language model and NLTK (tokenizer, POS, NER, VADER) on the same passage and compares them | LangChain, NLTK |

Main findings: cleaning leaves 147 useful tokens but removes negation words; lemmatization gives readable words but needs POS tags; NLTK NER got 3 of 10 predictions right; the language model called the passage neutral while VADER scored it negative (compound −0.8847).

## Installation instructions
Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.10+ if needed).

1. Clone the repository and open this folder:
   ```bash
   git clone <your-repository-url>
   cd lab-09-business-text-analytics-update
   ```
2. Install the dependencies for the script:
   ```bash
   uv sync
   ```
3. **Notebook in Google Colab (recommended):** upload `business_text_analytics.ipynb` and `business_text_data.txt` to Colab (the notebook reads `/content/business_text_data.txt`). In VS Code you can instead install the **Google Colab** extension, open the notebook, and choose **Select Kernel > Colab > New Colab Server**.
4. **Groq API key (Requirements 5–7):** create a free key at [console.groq.com](https://console.groq.com), then in Colab open **Secrets** (key icon), add `GROQ_API_KEY`, and turn on notebook access. The notebook reads it with `userdata.get("GROQ_API_KEY")`. **Never write the key in the code, outputs or screenshots, and never commit it.**

## Required dependencies
| Where | Packages |
|---|---|
| Script (`uv sync`) | `nltk>=3.9` |
| Notebook on your own computer (`uv sync --group notebook`) | `pandas`, `ipykernel` |
| Notebook on Colab (installed by the notebook) | `nltk`, `langchain-groq` (brings in `langchain-core`, `groq`) |

NLTK data used: `punkt`, `punkt_tab`, `stopwords`, `wordnet`, `averaged_perceptron_tagger`, `averaged_perceptron_tagger_eng`, `maxent_ne_chunker`, `maxent_ne_chunker_tab`, `words`, `vader_lexicon`. The notebook downloads them with `nltk.download(...)`.

## Commands for running the application
**Notebook (all requirements):** open `business_text_analytics.ipynb`, choose the Colab kernel, and select **Run All** (add `GROQ_API_KEY` to Secrets first).

**Script (NLTK steps and VADER sentiment, no API key needed):**
```bash
uv run python business_text_analysis01.py
```
Save the output to a file (PowerShell):
```powershell
uv run python business_text_analysis01.py | Out-File -Encoding utf8 outputs\script_output.txt
```
Bash/macOS/Linux:
```bash
uv run python business_text_analysis01.py > outputs/script_output.txt
```

## Description of the expected output
- **Dataset:** `Number of lines: 12`.
- **Tokenization (Req. 1):** for each text, the original line and its processed tokens, for example text 4 becomes `['logic', 'undeniable']`; 147 tokens in total.
- **Stemming and lemmatization (Req. 2):** original, stemmed and lemmatized tokens per text, for example `detective → detect` (stem) and `serves → serf` (default lemma, a known limitation).
- **NER (Req. 3):** a list of entities per text, such as `('Susan Calvin', 'PERSON')`; texts 1, 4, 6 and 10 return `[]`.
- **POS tagging (Req. 4):** `(word, tag)` pairs per text, for example `('did', 'VBD'), ('not', 'RB'), ('murder', 'VB')`.
- **Sentiment prompt (Req. 5–6):** the prompt template, then the model's label and short explanation for three sample sentences (positive, negative, neutral — 3 of 3 matched my expectation).
- **Pre-trained models (Req. 7):** the model's entities and sentiment for dataset text 2 (neutral), followed by NLTK tokens, POS tags, entities and the VADER scores (`compound −0.8847`).

Model wording can vary between runs and model versions.

## Screenshots
Screenshots of the executed notebook outputs are in [`screenshots/`](screenshots/). No API key appears in any of them.

| # | File | Shows |
|---|---|---|
| 1 | `01_dataset_and_tokenization.png` | Dataset load (12 lines) and Requirement 1 tokens |
| 2 | `02_stemming_lemmatization.png` | Requirement 2 stems and lemmas |
| 3 | `03_named_entity_recognition.png` | Requirement 3 NER |
| 4 | `04_pos_tagging.png` | Requirement 4 POS tags |
| 5 | `05_sentiment_prompt.png` | Requirement 5 sentiment prompt |
| 6 | `06_sentiment_three_samples.png` | Requirement 6 model results on three sentences |
| 7 | `07_llm_on_dataset_passage.png` | Requirement 7 language model on dataset text 2 |
| 8 | `08_nltk_on_same_passage.png` | Requirement 7 NLTK and VADER on the same passage |

## Project files
| File | Purpose |
|---|---|
| `business_text_data.txt` | The dataset (12 lines) |
| `business_text_analytics.ipynb` | Executed notebook for Requirements 1–7 with outputs |
| `business_text_analysis01.py` | NLTK script (tokenization, stemming, lemmatization, POS, NER, VADER) |
| `outputs/` | Text copies of the notebook outputs (`01_…` to `08_…`) |
| `screenshots/` | Screenshots of the notebook outputs |
| `pyproject.toml`, `uv.lock` | uv project and locked dependencies |
| `.gitignore` | Keeps `.venv`, caches, `.env` and key files out of Git |

## Notes
- Sentiment is analysed on the original text, because stop-word removal drops negations such as *not*.
- The sentiment tests are small (3 sentences and 1 passage), so they do not measure accuracy. A person should review model output before business decisions.
- If an API key is ever exposed, delete it in the Groq console and create a new one.
