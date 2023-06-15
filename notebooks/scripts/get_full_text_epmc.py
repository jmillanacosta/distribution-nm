import requests
import re
import numpy as np
import json

def get_full_text(id, check =False):

    base_url_text = "https://www.ebi.ac.uk/europepmc/webservices/rest/{}/fullTextXML"
    USER_AGENT = "Mozilla/5.0"
    url = base_url_text.format(id)
    # Request text
    response = requests.get(url, headers={"User-Agent": USER_AGENT})
    response_code = response.status_code
    try:
        if response_code < 200 or response_code >= 300:
            print(f"Failed to retrieve data for {id}. Response code: {str(response_code)} / url: {url}")
            pass
        else:
            response_text = response.text

            cleaned_text = re.sub("<.*?>", "", response_text)  #remove all XML tags
            cleaned_text = re.sub("&[#\\w]+?;", "", cleaned_text) #remove HTML entities
            cleaned_text = re.sub("\\s+", " ", cleaned_text) #replace multiple whitespaces with a single space
            cleaned_text = cleaned_text.replace(">", "") # leftfromthe    body tag if <body>
            cleaned_text = cleaned_text.strip()  #  removeleadingtrailing whitespaces
            return cleaned_text
    except Exception as e:
        print(f"Not available: {id} / " + str(e))
        pass

def check_full_texts(ids):
    available = []
    for id in ids:
        is_ft = get_full_text(id, check = True)
        if is_ft:
            print(id)
            available.append(id)
    return available