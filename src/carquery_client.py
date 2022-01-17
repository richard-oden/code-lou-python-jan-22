import client_helper as helper

def get_carquery_json(url):
    return helper.get_json(url, {'User-Agent': 'PostmanRuntime/7.29.0'}) #for some reason I get a 403 error unless I mimic postman ¯\_(ツ)_/¯

def get_years():
    return get_carquery_json('https://www.carqueryapi.com/api/0.3/?cmd=getYears')

def get_makes(year):
    return get_carquery_json(f'https://www.carqueryapi.com/api/0.3/?cmd=getMakes&year={year}')

def get_models(year, make):
    return get_carquery_json(f'https://www.carqueryapi.com/api/0.3/?cmd=getModels&year={year}&make={make}')

def get_trims(year, make, model):
    return get_carquery_json(f'https://www.carqueryapi.com/api/0.3/?cmd=getTrims&&year={year}&make={make}&model={model}&full_results=0')

def get_model(model_id):
    return get_carquery_json(f"https://www.carqueryapi.com/api/0.3/?cmd=getModel&model={model_id}")