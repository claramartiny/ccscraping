import feedparser


def fetch_green_feed():
    # Fetch LeMonde's climat RSS feed, and return the latest 5 links of articles.

    # Import LeMonde's climat RSS feed.
    data = feedparser.parse('feed:https://www.lemonde.fr/climat/rss_full.xml')

    # We only want to fetch the latest 5 links.

    cc_links = []

    for entry in data.entries[:5]:
        cc_links.append(entry.link)

    return cc_links
    





