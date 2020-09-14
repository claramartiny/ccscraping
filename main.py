from step1_link import fetch_green_feed
from step2_summarize import summarize_text
from step3_sendemail import send_email
from dotenv import load_dotenv

    #dotenv loads a secret file from computer.

def main():
    # Main entry point of `ccscraping`.

    # Load environment secrets.
    load_dotenv()

    # Step 1: import the links.
    cc_links = fetch_green_feed()

    # Step 2: sumarize each article from each link.
    
    articles=[]
    
    for link in cc_links:
        
        objet = summarize_text(link)
        #print(objet.title)
        articles.append(objet)

    # Step 3: send the summarized articles into an email.

    send_email(articles)


    






if __name__ == "__main__":
    main()

