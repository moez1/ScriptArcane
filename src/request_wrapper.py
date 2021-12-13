import logging

import requests

from src.utils.url import get_url_with_params

_LOGGER = logging.getLogger(__name__)


class HttpClient:

    def get(
        self,
        url: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None,
        json: dict = None,
    ):
        url = get_url_with_params(url, params)
        _LOGGER.debug(f"GET : {url}, param: {params}")
        response = requests.get(url, data=data, headers=headers)
        _LOGGER.debug(f"Response : {response.json}")
        return response

