import requests
import re
import numpy as np
import json

def get_full_text(id):

    base_url_text = "https://www.ebi.ac.uk/europepmc/webservices/rest/{}/fullTextXML"
    USER_AGENT = "Mozilla/5.0"
    url = base_url_text.format(id)
    # Request text
    response = requests.get(url, headers={"User-Agent": USER_AGENT})
    response_code = response.status_code
    try:
        if response_code < 200 or response_code >= 300:
            #print(f"Failed to retrieve data for {id}. Response code: " +str(response_code))
            pass
        else:
            response_text = response.text
            body_content = ""
            regex = "<body(.*?)</body"
            pattern = re.compile(regex, re.DOTALL)
            matcher = pattern.search(response_text)
            if matcher:
                body_content = matcher.group(1)
                cleaned_text = re.sub("<.*?>", "", body_content)  #remove  all XML tags
                cleaned_text = re.sub("&[#\\w]+?;", "", cleaned_text)  #remove HTML entities
                cleaned_text = re.sub("\\s+", " ", cleaned_text)  #replace multiple whitespaces with a single space
                cleaned_text = cleaned_text.replace(">", "") # left fromthe body tag if <body>
                cleaned_text = cleaned_text.strip()  #  remove leadingtrailing whitespaces
                return cleaned_text
    except Exception as e:
        #print(f"An error occurred for {id}: " + str(e))
        pass