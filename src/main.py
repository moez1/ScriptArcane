import logging
from logging import config
from models.base import session
from models.tweets_metric import TweetsMetric, TweetsMetricQuerys

from src.request_wrapper import HttpClient
from src.config import log_config, BEARER_TOKEN


config.dictConfig(log_config)
_LOGGER = logging.getLogger(__name__)

http_client = HttpClient()


def get_tweet_ids():
    """ function for get all tweet id

    Returns:
        tweet(liste): [liste of tweet id]
    """
    headers = {"Authorization": f"BEARER {BEARER_TOKEN}"}
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        "query": "#Arcane"
    }

    result = http_client.get(url, headers=headers, params=params)

    result_json = result.json()

    tweet_ids = list(map(lambda x: x["id"], result_json["data"]))

    return tweet_ids


def get_public_metrics():
    """function for get all data (text of tweet,
     number of like, number of retweet, 
     number of response,number of views video)

    Returns:
        result (dict): [dict of data]
    """
    headers = {"Authorization": f"BEARER {BEARER_TOKEN}"}
    url = "https://api.twitter.com/2/tweets"
    tweet_ids = ",".join(get_tweet_ids())
    params = {
        "ids": tweet_ids,
        "tweet.fields": "public_metrics",
        "expansions": "attachments.media_keys",
        "media.fields": "public_metrics"
    }

    result = http_client.get(url, headers=headers, params=params)

    return result.json()


if __name__ == "__main__":
    """the main when we insert data in Database
    """
    tweet_metrics_query = TweetsMetricQuerys()
    public_metrics = get_public_metrics()
    public_metrics_data = public_metrics["data"]
    public_metrics_medias = public_metrics["includes"]["media"]

    tweet_metrics = []
    media = []
    for item in public_metrics_data:
        tweet_metric = TweetsMetric(item["id"], item["text"], item["public_metrics"]["like_count"],
                                    item["public_metrics"]["retweet_count"], item["public_metrics"]["reply_count"])
        try:
            media_keys = item["attachments"]["media_keys"]
            for media_key in media_keys:
                media = list(filter(
                    lambda x: x["media_key"] == media_key and x["type"] == "video", public_metrics_medias))
        except KeyError:
            pass

        if media:
            tweet_metric.video_view_number = media[0]["public_metrics"]["view_count"]

        tweet_metrics.append(tweet_metric)

    for item in tweet_metrics:
        session.add(item)
        session.commit()

    session.close()
