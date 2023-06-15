import requests
import re
import numpy as np
import json

def get_abstract(id):

    base_url_text = "https://www.ebi.ac.uk/europepmc/webservices/rest/article/PMC/{}?resultType=core&format=json"
    USER_AGENT = "Mozilla/5.0"
    url = base_url_text.format(id)
    # Request text
    response = requests.get(url, headers={"User-Agent": USER_AGENT})
    response_code = response.status_code
    try:
        if response_code < 200 or response_code >= 300:
            print(f"Non-200 response code for {id}")
            return ""
        else:
            abstract = response.json()['result']['abstractText']
            return abstract
    except Exception as e:
        print(f"Not available: ({str(e)}) for {id}")
        return ""
        pass