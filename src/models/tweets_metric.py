import logging

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import MetaData, Table

from src.models.base import Base, session, engine

_LOGGER = logging.getLogger(__name__)


class TweetsMetric(Base):
    __tablename__ = 'tweets_metric'
    __table_args__ = {'extend_existing': True}

    tweet_id = Column(Integer, primary_key=True)
    text = Column(String)
    like_number = Column(Integer)
    retweet_number = Column(Integer)
    response_number = Column(Integer)
    video_view_number = Column(Integer)


    def __init__(self, tweet_id=None, text=None, like_number=None, retweet_number=None, response_number=None, video_view_number=None):
        self.tweet_id = tweet_id
        self.text = text
        self.like_number = like_number
        self.retweet_number = retweet_number
        self.response_number = response_number
        self.video_view_number = video_view_number


class TweetsMetricQuerys:

    def create(obj):
        try:
            session.add(obj)
            session.commit()
            session.close()
        except Exception:
            _LOGGER.error(Exception, exc_info=True)
            raise Exception
