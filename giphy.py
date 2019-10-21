import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import webbrowser


def gifGenerator(txt, results):
    # create an instance of the API class
    api_instance = giphy_client.DefaultApi()
    api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
    q = txt # str | Search query term or prhase.
    limit = results # int | The maximum number of records to return. (optional) (default to 25)
    offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

    try: 
        # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, lang=lang, fmt=fmt)
        x = api_response.data
        for gif in x:
            y = gif
            webbrowser.open(y.images.downsized.url)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
    
