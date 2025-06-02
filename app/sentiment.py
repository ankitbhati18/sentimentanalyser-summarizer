from textblob import TextBlob
from googletrans import Translator
import pyttsx3
from transformers import pipeline
from googletrans import Translator




# Initialize translator and summarizer
translator = Translator()
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")
def analyze_sentiment(text, target_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    sentiment = 'positive' if 'good' in translated.text.lower() else 'negative'
    return translated.text, sentiment

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity >= 0.6:
        return 'Very Positive 😊'
    elif polarity >= 0.2:
        return 'Positive 🙂'
    elif polarity > -0.2:
        return 'Neutral 😐'
    elif polarity > -0.6:
        return 'Negative 🙁'
    else:
        return 'Very Negative 😠'

def translate_text(text, dest_language):
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def text_to_speech(text, filename='app/static/audio/output.mp3'):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename

def summarize_text(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
