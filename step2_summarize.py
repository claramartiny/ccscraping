import newspaper
import nltk
from newspaper import Article

nltk.download('punkt')

def summarize_text(link):

    article = Article(link,language='fr')
    article.download()
    article.parse()
    article.nlp()

    return(article)
