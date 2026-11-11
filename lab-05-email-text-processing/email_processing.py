"""Hands-on text processing for email management (GLAB 927.1.2).

Compares stemming and POS-aware lemmatization on business emails and adds
a simple keyword-based email categorizer.
"""

import nltk
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer

RESOURCES = [
    "punkt",
    "punkt_tab",
    "wordnet",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
]

EMAIL_STEM = (
    "Our team will be working on the upcoming project deadlines. "
    "Please ensure that all deliverables are submitted before the end of the week."
)
EMAIL_LEMMA = (
    "The team members are working on their tasks diligently. "
    "Please ensure that every report is submitted promptly."
)

CATEGORIES = {
    "billing": {"invoice", "payment", "charge", "refund", "bill"},
    "technical issues": {"error", "bug", "crash", "login", "server", "fail"},
    "customer support": {"help", "support", "issue", "problem", "assist"},
}


def download_resources() -> None:
    for name in RESOURCES:
        nltk.download(name, quiet=True)


def to_wordnet_pos(treebank_tag: str) -> str:
    """Map a Penn Treebank POS tag to a WordNet POS constant."""
    if treebank_tag.startswith("J"):
        return wordnet.ADJ
    if treebank_tag.startswith("V"):
        return wordnet.VERB
    if treebank_tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN


def stem_text(text: str) -> list[str]:
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in nltk.word_tokenize(text)]


def lemmatize_default(text: str) -> list[str]:
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in nltk.word_tokenize(text)]


def lemmatize_pos(text: str) -> list[str]:
    lemmatizer = WordNetLemmatizer()
    tagged = nltk.pos_tag(nltk.word_tokenize(text))
    return [lemmatizer.lemmatize(w, to_wordnet_pos(t)) for w, t in tagged]


def categorize(text: str) -> str:
    """Classify an email by matching lemmas against category keywords."""
    lemmas = {w.lower() for w in lemmatize_pos(text)}
    scores = {cat: len(lemmas & kws) for cat, kws in CATEGORIES.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "general inquiry"


def compare(text: str) -> None:
    tokens = nltk.word_tokenize(text)
    stems = stem_text(text)
    default = lemmatize_default(text)
    pos = lemmatize_pos(text)
    print(f"{'Token':<14}{'Stem':<14}{'Lemma (noun)':<16}{'Lemma (POS)':<14}")
    print("-" * 58)
    for row in zip(tokens, stems, default, pos):
        print(f"{row[0]:<14}{row[1]:<14}{row[2]:<16}{row[3]:<14}")


def main() -> None:
    download_resources()
    print(f"NLTK version: {nltk.__version__}\n")

    print("=== Task 2: Stemming ===")
    print("Original:", EMAIL_STEM)
    print("Stemmed: ", " ".join(stem_text(EMAIL_STEM)), "\n")

    print("=== Task 3: Lemmatization (POS-aware) ===")
    print("Original:  ", EMAIL_LEMMA)
    print("Lemmatized:", " ".join(lemmatize_pos(EMAIL_LEMMA)), "\n")

    print("=== Comparison: stemming vs. lemmatization ===")
    compare(EMAIL_LEMMA)
    print(
        "\nNote: stemming is faster but can produce non-words (e.g., 'promptli'); "
        "lemmatization returns real dictionary words and is better when meaning matters.\n"
    )

    print("=== Bonus: email categorization ===")
    samples = [
        "I was charged twice on my last invoice, please refund the payment.",
        "The server keeps crashing and I get a login error.",
        "Can you tell me your office hours?",
    ]
    for s in samples:
        print(f"[{categorize(s)}] {s}")


if __name__ == "__main__":
    main()