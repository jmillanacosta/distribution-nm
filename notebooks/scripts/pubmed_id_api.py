import re
import requests

def get_identifier_type(identifier):
    identifier = str(identifier)
    if 'doi' in identifier:
        return 'doi'
    elif re.match(r'\d+', identifier):
        return 'pmid'
    elif 'http' in identifier:
        return 'other_url'
    else:
        return None



def id_convert(ids):
    service_root = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?tool=distribution-nm&email=javier.millanacosta@maastrichtuniversity.nl&ids={}&format=json"
    USER_AGENT = "Mozilla/5.0"
    url = service_root.format(ids)
    response = requests.get(url, headers={"User-Agent": USER_AGENT})
    response_code = response.status_code
    try:
        if response_code < 200 or response_code >= 300:
            #print(f"Non-200 response code for {url}")
            return False
        else:
            
            if 'pmcid' in response.json()['records'][0].keys():
                
                pmcid = response.json()['records'][0]['pmcid']
                if 'doi' in response.json()['records'][0].keys(): 
                    doi = response.json()['records'][0]['doi']
                else:
                    doi = ""
                return(pmcid, doi)
            else:
                return False
                
    except Exception as e:
        #print(f"An error ({str(e)}) occurred for {id}")
        return False


def convert_to_pmcid(row):
    if row['identifier_type'] in ['pmid', 'doi']:
        return id_convert(row['provided_identifier'])
    else:
        return None
    
def id_set(df):
    seen = []
    for index, row in df.iterrows():
        id = row['provided_identifier']
        if id not in seen:
            seen.append(id)
            converted = id_convert(id)
            if converted != False:
                pmcid = converted[0]
                doi = converted[1]
                df.at[index, 'pmcid'] = pmcid
                df.at[index, 'doi'] = doi
    return df
