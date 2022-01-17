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