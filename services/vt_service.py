import requests
import base64

VT_API_KEY = "7af36614993d2875e516edaa97ba3904c1fd4762889ddc9262810c4f539c5c64"

def check_virustotal(indicador, tipo):

    headers = {
        "x-apikey": VT_API_KEY
    }

    base_url = "https://www.virustotal.com/api/v3"

    if tipo == "ip":
        url = f"{base_url}/ip_addresses/{indicador}"

    elif tipo == "domain":
        url = f"{base_url}/domains/{indicador}"

    elif tipo == "url":
        url_id = base64.urlsafe_b64encode(indicador.encode()).decode().strip("=")
        url = f"{base_url}/urls/{url_id}"

    elif tipo == "hash":
        url = f"{base_url}/files/{indicador}"

    else:
        return {"vt_malicious": 0, "vt_suspicious": 0}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]

        return {
            "vt_malicious": stats.get("malicious", 0),
            "vt_suspicious": stats.get("suspicious", 0)
        }

    return {"vt_malicious": 0, "vt_suspicious": 0}