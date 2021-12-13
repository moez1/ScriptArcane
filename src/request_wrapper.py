import logging

import requests

from src.utils.url import get_url_with_params

_LOGGER = logging.getLogger(__name__)


class HttpClient:
    """Class for get data from API tweeter
    """

    def get(
        self,
        url: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None,
        json: dict = None,
    ):
        """ function for get data. 

        Args:
            url (str): [url of api]
            params (dict, optional): [params of api]. Defaults to None.
            data (dict, optional): [data of api]. Defaults to None.
            headers (dict, optional): [header of api]. Defaults to None.
            json (dict, optional): [json of api]. Defaults to None.

        Returns:
            response (dict): [data from api]
        """
        url = get_url_with_params(url, params)
        _LOGGER.debug(f"GET : {url}, param: {params}")
        response = requests.get(url, data=data, headers=headers)
        _LOGGER.debug(f"Response : {response.json}")
        return response
