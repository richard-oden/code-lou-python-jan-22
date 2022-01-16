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

def get_vehicle_id(make, model, year):
    return get_json(
        f"https://www.carqueryapi.com/api/0.3/?cmd=getTrims&make={make}&model={model}&year={year}&full_results=0", 
        {'User-Agent': 'PostmanRuntime/7.29.0'})['Trims']#[0]['model_id'] #for some reason I get a 403 error unless I mimic postman ¯\_(ツ)_/¯

def get_vehicle_details(vehicle_id):
    return get_json(
        f"https://www.carqueryapi.com/api/0.3/?cmd=getModel&model={vehicle_id}", 
        {'User-Agent': 'PostmanRuntime/7.29.0'})

def get_specific_vehicle_data(make, model, year):
    details = get_vehicle_details(get_vehicle_id(make, model, year))
    return list(map(lambda d: 
        { 
            'make': d['make_display'],
            'model': d['model_name'],
            'year': d['model_year'] and int(d['model_year']),
            'mpg_highway': d['model_mpg_hwy'] and float(d['model_mpg_hwy']),
            'mpg_city': d['model_mpg_city'] and float(d['model_mpg_city']),
            'mpg_mixed': d['model_mpg_mixed'] and float(d['model_mpg_mixed']),
            'fuel_capacity_gal': d['model_fuel_cap_g'] and float(d['model_fuel_cap_g']),
            'lkm_highway': d['model_lkm_hwy'] and float(d['model_lkm_hwy']),
            'lkm_city': d['model_lkm_city'] and float(d['model_lkm_city']),
            'lkm_mixed': d['model_lkm_mixed'] and float(d['model_lkm_mixed']),
            'fuel_capacity_l': d['model_fuel_cap_l'] and float(d['model_fuel_cap_l']),
            'fuel_type': d['model_engine_fuel']
        }, details))[0]


print(get_vehicle_id('subaru', 'outback', 2012))