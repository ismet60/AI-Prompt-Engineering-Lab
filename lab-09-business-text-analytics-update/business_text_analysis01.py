"""Analyze the Business text with NLTK."""
from pathlib import Path
import string
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer, WordNetLemmatizer

RESOURCES = ('punkt_tab', 'stopwords', 'wordnet', 'averaged_perceptron_tagger_eng', 'maxent_ne_chunker_tab', 'words', 'vader_lexicon')
for resource in RESOURCES:
    if not nltk.download(resource, quiet=True):
        raise RuntimeError(f'Unable to download NLTK resource: {resource}')

source = Path(__file__).with_name('business_text_data.txt')
records = [line.strip() for line in source.read_text(encoding='utf-8').splitlines() if line.strip()]
stop = set(stopwords.words('english'))
stemmer, lemmatizer = PorterStemmer(), WordNetLemmatizer()
sentiment = SentimentIntensityAnalyzer()
print('Dataset:', source.name, '| Nonempty records:', len(records))
print('Note: NER and POS use original text; sentiment uses original text to preserve context.')
for i, text in enumerate(records, 1):
    tokens = word_tokenize(text)
    clean = [w.lower() for w in tokens if w.isalpha() and w.lower() not in stop and w not in string.punctuation]
    tagged = pos_tag(tokens)
    tree = ne_chunk(tagged)
    entities = [(' '.join(word for word, tag in node.leaves()), node.label()) for node in tree if isinstance(node, nltk.Tree)]
    score = sentiment.polarity_scores(text)['compound']
    label = 'positive' if score >= 0.05 else 'negative' if score <= -0.05 else 'neutral'
    print(f'\n--- Record {i} ---')
    print('Original:', text)
    print('Processed tokens:', clean)
    print('Stems:', [stemmer.stem(w) for w in clean])
    print('Lemmas (default noun):', [lemmatizer.lemmatize(w) for w in clean])
    print('POS:', tagged)
    print('Named entities:', entities)
    print(f'VADER sentiment: {label} (compound={score:.4f})')
