import newspaper
import nltk
from newspaper import Article

nltk.download('punkt')

def summarize_text(link):

    article = Article(link,language='fr')
    article.download()
    article.parse()
    article.nlp()

    return(article.summary)

#aaa = summarize_text('https://www.lemonde.fr/societe/article/2020/09/10/covid-19-imbroglio-autour-des-masques-des-enseignants_6051702_3224.html')
#print(aaa)
