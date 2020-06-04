# Blockchain
Esta app es un intento por adaptar una app blockchain bastante sencilla proporcionada por IBM como forma de tutorial a un blockchain de diplomas de graduados.
</br>Link de IBM  --> https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/


## Instalar y correr por primera vez
- Clonar el repositorio: </br>
$git clone https://github.com/anonimeishon/Blockchain </br>

- Instalar los requerimientos para el correcto uso de la app por medio de Pip </br>
$pip install -r requirements.txt </br>

- Correr uno de los nodos a usar para el minado del nonce, esto puede probarse ya sea en la misma maquina en distintos puertos, o en otra </br>
cambiando el ip de host en el archivo Blockchain/app/views.py </br>
"CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"" </br>

$ export FLASK_APP=node_server.py
$ flask run --port 8000

- Ya que tenemos un nodo del blockchain corriendo, lanzaremos la aplicacion en otra terminal/maquina </br>
$ python run_app.py </br>

- Para añadir aun mas maquinas o nodos, simplemente lanzamos el nodo donde sea deseado y se modifica el siguiente comando de acuerdo a las necesidades </br>
$ curl -X POST \
  http://127.0.0.1:8001/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'
</br>

donde -d es nuestro primer nodo, y lo primero es el nodo a conectar. </br>

- Una vez corrida la app, la informacion de los bloques debe estar guardada en la ruta /chain de cualquiera de los nodos </br>
o, tambien puede ser visualizada de la siguiente manera: </br>

$ curl -X GET http://127.0.0.1:8000/chain
</br>
