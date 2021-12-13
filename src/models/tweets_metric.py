import logging

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import MetaData, Table

from src.models.base import Base, session, engine

_LOGGER = logging.getLogger(__name__)


class TweetsMetric(Base):
    """ class for create database
    """
    __tablename__ = 'tweets_metric'
    __table_args__ = {'extend_existing': True}

    tweet_id = Column(Integer, primary_key=True)
    text = Column(String)
    like_number = Column(Integer)
    retweet_number = Column(Integer)
    response_number = Column(Integer)
    video_view_number = Column(Integer)

    def __init__(self, tweet_id=None, text=None, like_number=None, retweet_number=None, response_number=None, video_view_number=None):
        """ function constructor TweetsMetric

        Args:
            tweet_id ([int], optional): [tweet id]. Defaults to None.
            text ([str], optional): [text of tweet]. Defaults to None.
            like_number ([int], optional): [like number of tweet]. Defaults to None.
            retweet_number ([int], optional): [description]. Defaults to None.
            response_number ([int], optional): [number of response]. Defaults to None.
            video_view_number ([int], optional): [number of views]. Defaults to None.
        """
        self.tweet_id = tweet_id
        self.text = text
        self.like_number = like_number
        self.retweet_number = retweet_number
        self.response_number = response_number
        self.video_view_number = video_view_number


class TweetsMetricQuerys:
    """class for create object in Database.
    """

    def create(obj):
        """class for create Data in Database 

        Args:
            obj ([objet]): [object of instance class TweetsMetric]

        Raises:
            Exception: [for catch error]
        """
        try:
            session.add(obj)
            session.commit()
            session.close()
        except Exception:
            _LOGGER.error(Exception, exc_info=True)
            raise Exception
