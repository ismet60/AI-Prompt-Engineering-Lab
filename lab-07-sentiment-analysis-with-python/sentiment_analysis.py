# GLAB 927.4.1 - Hands-On Sentiment Analysis with Python (TextBlob)

# ---------- Task 1: Importing Libraries ----------
# TextBlob provides a simple API for sentiment analysis
from textblob import TextBlob

# Sample text to confirm TextBlob is installed
sample_text = "TextBlob is successfully installed and ready to use!"
print(f"TextBlob library successfully imported. Sample text: {sample_text}")
print("-----")

# ---------- Task 2: Implementing Sentiment Analysis ----------
sample_text = "I absolutely love this product! The quality is excellent and it arrived on time."

# Create a TextBlob object
blob = TextBlob(sample_text)

# Perform sentiment analysis
sentiment = blob.sentiment

print("Original Text:", sample_text)
print("Sentiment Analysis Result:")
print("Polarity:", sentiment.polarity)          # -1 (negative) to 1 (positive)
print("Subjectivity:", sentiment.subjectivity)  # 0 (objective) to 1 (subjective)
print("-----")

# ---------- Task 3: Analyzing Business Communication Data ----------
feedback_comments = [
    "The service was fantastic and the staff was very helpful.",
    "I am unhappy with the product quality and delivery was delayed.",
    "The product is okay, but it could be improved.",
    "Amazing experience! I am very satisfied with my purchase.",
]

# Function to get the polarity score of a comment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Analyze and print sentiment for each feedback comment
for comment in feedback_comments:
    sentiment = analyze_sentiment(comment)
    print(f"Feedback: {comment}")
    print(f"Sentiment Polarity: {sentiment}")
    print("-----")
