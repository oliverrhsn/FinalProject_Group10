import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cpsfq69r01qkode1eea0cpsfq69r01qkode1eeag")

    news = finnhub_client.general_news('general', min_id=0)

    return news