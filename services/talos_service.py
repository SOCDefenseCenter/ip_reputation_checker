import requests

def check_talos(ip):
    try:
        url = f"https://talosintelligence.com/sb_api/query_lookup?query={ip}&type=ip"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers, timeout=10)
        print("STATUS TALOS:", response.status_code)
        print("RAW TEXT TALOS:", response.text)

        if response.status_code == 200:

            # 👇 AQUÍ VA
            data = response.json()

            print("Respuesta Talos:", data)  # 👈 línea para depurar

            reputation = (
                data.get("data", {})
                    .get("reputation")
            )

            if reputation is None:
                return {"talos_reputation": "-"}

            if reputation < 0:
                reputacion_texto = "Mala"
            elif reputation == 0:
                reputacion_texto = "Neutral"
            else:
                reputacion_texto = "Buena"

            return {
                "talos_reputation": reputacion_texto
            }

        return {"talos_reputation": "-"}

    except Exception as e:
        print("Error Talos:", e)
        return {"talos_reputation": "-"}