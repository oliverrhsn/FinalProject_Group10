import mongodb_loader
import pandas as pd
from sentiment_analysis import SentimentAnalysis
import postgres_loader

def run():
    db = mongodb_loader.get_data("news", "finnhub_news")

    news = [x for x in db.finnhub_news.find()]

    output = []
    for news_summary in news:
        output.append(SentimentAnalysis(text=news_summary["summary"]).execute())

        print(f"Summary {news_summary['summary']} successfully analized")

    sentiment_output = pd.DataFrame(output)

    postgres_loader.load(sentiment_output, "sentiment_news_analysis")

    print("Successfully loaded to Postgres")

if __name__ == "__main__":
    run()