import urllib


def get_url_with_params(url: str, params: dict = None):
    """function for create url with params

    Args:
        url (str): [url for get]
        params (dict, optional): [params of Url]. Defaults to None.

    Returns:
        url (str): [url with all params]
    """
    if params:
        params_str = urllib.parse.urlencode(params, True)
        return f"{url}?{params_str}"
    return url
