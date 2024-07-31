import spacy
from textblob import TextBlob
import readability

nlp = spacy.load("en_core_web_sm")

def analyze_profile(profile_text):
    doc = nlp(profile_text)
    sentiment = TextBlob(profile_text).sentiment
    readability_score = readability.getmeasures(profile_text, lang='en')
    
    keywords = [token.lemma_ for token in doc if token.is_stop != True and token.is_punct != True]
    keyword_freq = {}
    for keyword in keywords:
        if keyword in keyword_freq:
            keyword_freq[keyword] += 1
        else:
            keyword_freq[keyword] = 1
    
    sorted_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)
    
    analysis = {
        "sentiment_polarity": sentiment.polarity,
        "sentiment_subjectivity": sentiment.subjectivity,
        "readability_score": readability_score['readability grades']['FleschReadingEase'],
        "keywords": sorted_keywords[:10]
    }
    
    return analysis

profile_text = """
I love hiking and exploring new places. On weekends, you'll find me at the beach or trying out a new restaurant. 
I'm passionate about photography and enjoy capturing moments. Looking for someone who shares similar interests and values.
"""

result = analyze_profile(profile_text)
print(result)
