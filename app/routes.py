from flask import Blueprint, render_template, request
from .sentiment import analyze_sentiment, translate_text, text_to_speech, summarize_text


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    dest_language = request.form.get('language', 'en')

    sentiment = analyze_sentiment(text)
    translated_text = translate_text(text, dest_language)
    summary = summarize_text(text)
    audio_file = text_to_speech(translated_text)

    return render_template('result.html', 
                           original_text=text, 
                           translated_text=translated_text, 
                           sentiment=sentiment, 
                           summary=summary, 
                           audio_file=audio_file)
