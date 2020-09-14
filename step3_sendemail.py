import os
import requests

def send_email(articles):

	text=""

	for article in articles:
		text=text+article.title+"\n"+article.summary+"\n"+"\n"+"\n"

	return requests.post(
		os.getenv("MAILGUN_URL"),
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={"from": os.getenv("EMAIL"),
			"to": os.getenv("EMAIL"),
			"subject": "Le Monde - Climat",
			"text": text})