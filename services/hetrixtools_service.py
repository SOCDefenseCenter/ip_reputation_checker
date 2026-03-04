import requests

HETRIX_API_KEY = "c0f37e0e05e9eb4204aa40dfe9d86079"

def check_hetrixtools(ip):

    url = f"https://api.hetrixtools.com/v1/c0f37e0e05e9eb4204aa40dfe9d86079/uptime/monitors/0/30/"
    
    params = {
        "host": ip
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("HETRIX HTTP ERROR:", response.status_code, response.text)
        return {"blacklists": 0}

    data = response.json()

    if data.get("status") != "success":
        print("HETRIX API FAIL:", data)
        return {"blacklists": 0}

    blacklisted_count = data.get("blacklisted_count", 0)

    return {
        "blacklists": int(blacklisted_count)
    }