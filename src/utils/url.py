import urllib

def get_url_with_params(url: str, params: dict = None) -> str:
    if params:
        params_str = urllib.parse.urlencode(params, True)
        return f"{url}?{params_str}"
    return url