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
            
# a=GeoAPI()
# print(a.is_hot_in_pehuajo())


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
# print(is_product_available("Granizado",11))



AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    c=0
    err=0
    if discount_code in AVAILABLE_DISCOUNT_CODES:
        return True
    else:
        for code in AVAILABLE_DISCOUNT_CODES:

            c=-1
            err=0
            for x in discount_code:
                c=c+1
                y = code[c]
                if x != y:
                    err=err+1
            if err < 3:
                return True
    return False

print(validate_discount_code("verano2021"))

# Ejemplo:"primavera2021" deberia devolver True, ya que al compararlo:
# vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P") 
# vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o', 'm', 'V', 'p', 'v')
# vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0', 'x', 'e', 'd', 'p', 'r')
# vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i', 'v', 'n','o', 'm', '2',