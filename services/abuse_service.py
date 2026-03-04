import requests
import pycountry

ABUSE_API_KEY = "79272deb97700230e0e39037017dbcbe1e5efebe79447335e014079373c6b488071c538ff31d5166"

def traducir_pais_a_espanol(nombre_ingles):
    traducciones = {
        "United States": "Estados Unidos",
        "China": "China",
        "Russia": "Rusia",
        "Germany": "Alemania",
        "France": "Francia",
        "Brazil": "Brasil",
        "India": "India",
        "United Kingdom": "Reino Unido",
        "Netherlands": "Países Bajos",
        "Canada": "Canadá",
        "Spain": "España",
        "Italy": "Italia",
        "Japan": "Japón",
        "South Korea": "Corea del Sur",
        "Mexico": "México",
        "Argentina": "Argentina",
        "Colombia": "Colombia",
        "Chile": "Chile",
        "Peru": "Perú",
        "Venezuela": "Venezuela"
    }

    return traducciones.get(nombre_ingles, nombre_ingles)

def obtener_nombre_pais(code):
    try:
        country = pycountry.countries.get(alpha_2=code)
        if country:
            nombre_ingles = country.name
            return traducir_pais_a_espanol(nombre_ingles)
        return "Desconocido"
    except:
        return "Desconocido"

def check_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Accept": "application/json",
        "Key": ABUSE_API_KEY
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()["data"]

            country_code = data.get("countryCode", None)
            country_name = obtener_nombre_pais(country_code) if country_code else "Desconocido"

            return {
                "abuse_score": data.get("abuseConfidenceScore", 0),
                "country": country_name
            }

        else:
            print("Error AbuseIPDB:", response.status_code, response.text)

    except Exception as e:
        print("Excepción AbuseIPDB:", e)

    return {
        "abuse_score": 0,
        "country": "Desconocido"
    }