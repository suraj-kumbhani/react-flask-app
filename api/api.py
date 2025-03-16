import time
import urllib.request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup  # Corrected import
from flask import Flask, request

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('punkt_tab') 
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/api/summary', methods=['POST', 'GET'])
def get_summary():
    # Step 1: Get URL from JSON payload
    if request.method == 'POST':
        data = request.get_json()
        url = data.get('url') if data else None
    else:
        url = request.args.get('url')
    
    if not url:
        return {'error': 'URL parameter is required'}, 400

    # Step 2: Data collection from URL
    try:
        article_content = urllib.request.urlopen(url)
        article = article_content.read()
        article_parsed = BeautifulSoup(article, 'html.parser')
        title = article_parsed.find('title').text
        paragraphs = article_parsed.find_all('p')
    except Exception as e:
        return {'error': str(e)}, 500
    
    # Step 3: Extract and clean text
    text = ''
    for p in paragraphs:
        text += p.text

    # Step 4: Data clean-up
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha() and word not in stop_words]

    # Step 5: Tokenization
    sentences = sent_tokenize(text)

    # Step 6: Calculate word frequency
    word_freq = nltk.FreqDist(words)

    # Step 7: Calculate weighted frequency for each sentence
    sent_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_freq.keys():
                if len(sentence.split(" ")) < 30:
                    if sentence not in sent_scores.keys():
                        sent_scores[sentence] = word_freq[word]
                    else:
                        sent_scores[sentence] += word_freq[word]

    # Step 8: Create summary by choosing top 10% of weighted sentences
    total_sent = len(sentences)
    summary_size = round(total_sent * 0.1)
    summary = " ".join([sent[0] for sent in sorted(sent_scores.items(), key=lambda x: x[1], reverse=True)[:summary_size]])

    return {'title': title, 'url': url, 'gist': summary}

if __name__ == '__main__':
    app.run(debug=True)
