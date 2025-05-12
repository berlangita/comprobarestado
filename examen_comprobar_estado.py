import requests
def comprobar_estado():
    try:
        patata = requests.get('http://192.168.1.53:5000/estado')
        if patata.status_code == 200:
            return "ok" \
        else:
            return "error"
    except requests.exceptions.ConnectionError:
        return "fallo de conexion"
    