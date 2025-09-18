try:
    from LeIA import SentimentIntensityAnalyzer
except ImportError:
    # fallback de import (se o pacote nomear diferente)
    from leia_br import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def classify_sentiment(text: str) -> str:
    scores = analyzer.polarity_scores(text)
    compound = scores.get("compound", 0.0)
    if compound >= 0.05:
        return "POSITIVO"
    elif compound <= -0.05:
        return "NEGATIVO"
    else:
        return "NEUTRO"
