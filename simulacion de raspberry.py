import time
import requests

# contador
contador = 0

# contador hasta el infinito con delay
while True:
    contador += 1
    print(contador)
    time.sleep(1)
    r = requests.post('http://localhost:5000/agregar',
                      data={'tarea': contador})
