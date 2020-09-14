from step1_link import fetch_green_feed
from step2_summarize import summarize_text


def main():
    # Main entry point of `ccscraping`.

    # Step 1: import the links.
    cc_links = fetch_green_feed()

    # Step 2: sumarize each article from each link.
    for link in cc_links:
        summary = summarize_text(link)
        print(summary)

    # Step 3: send the summarized articles into an email.


if __name__ == "__main__":
    main()
