import requests, json
import pandas as pd

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={GeoAPI.LAT}&lon={GeoAPI.LON}&appid={GeoAPI.API_KEY}")
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]
            currentTemp = temp["temp"]
            currentTemp = str(currentTemp)[0:2]
            return(int(currentTemp))


_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado","Limon", "Dulce de Leche"], 
                            "quantity":     [3,             10,            0,       5]})

def is_product_available(product_name, quantity):
    c=-1
    for x in( _PRODUCT_DF["product_name"]):
        c=c+1
        if x == product_name:
            if(_PRODUCT_DF.loc[c,"quantity"]) >= quantity:
                return True
    return False 



AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_worlds(w1,w2):
    c=-1
    err=0
    if len(str(w1))==len(str(w2)):
        for x in w1:
            c=c+1
            y = w2[c]
            if x != y:
                err=err+1
        return err
    else:
        return -1

def validate_discount_code(discount_code):
    errs=[]
    for code in AVAILABLE_DISCOUNT_CODES:
        err = validate_worlds(code, discount_code)
        errs.append(err)
    if 0 in errs or 1 in errs or 2 in errs:
        return True
    else:
        return False



