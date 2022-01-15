import requests

def get_json(url, headers={}):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as error:
        print(f'Other error occurred: {error}')
    else:
        return response.json()

def get_vehicle_details(make, model, year):
    return get_json(
        f"https://www.carqueryapi.com/api/0.3/?cmd=getTrims&make={make}&model={model}&year={year}", 
        {'User-Agent': 'PostmanRuntime/7.29.0'})['Trims'] #for some reason I get a 403 error unless I mimic postman ¯\_(ツ)_/¯


print(get_vehicle_details('subaru', 'outback', '2004'))