"""GLAB 927.1.2: normalize business email text with NLTK."""

import nltk
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer

# These resources support tokenization, tagging, and WordNet lemmatization.
for resource in ("punkt_tab", "averaged_perceptron_tagger_eng", "wordnet", "omw-1.4"):
    if not nltk.download(resource, quiet=True):
        raise RuntimeError(f"Could not download NLTK resource: {resource}")


def wordnet_pos(tag):
    """Convert Penn Treebank tags to WordNet's part-of-speech labels."""
    return {"J": wordnet.ADJ, "V": wordnet.VERB, "N": wordnet.NOUN, "R": wordnet.ADV}.get(tag[0], wordnet.NOUN)


def main():
    email = ("Our team will be working on the upcoming project deadlines. "
             "Please ensure that all deliverables are submitted before the end of the week.")
    tokens = nltk.word_tokenize(email)
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stemmed = [stemmer.stem(token) for token in tokens]
    lemmatized = [lemmatizer.lemmatize(token, wordnet_pos(tag))
                  for token, tag in nltk.pos_tag(tokens)]
    print("Original Email Content:", email)
    print("Stemmed Email Content:", " ".join(stemmed))
    print("Lemmatized Email Content:", " ".join(lemmatized))
    print("\nComparison (original | stem | lemma):")
    for original, stem, lemma in zip(tokens, stemmed, lemmatized):
        print(f"{original} | {stem} | {lemma}")


if __name__ == "__main__":
    main()
