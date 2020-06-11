# Blockchain
Esta app es un intento por adaptar una app blockchain bastante sencilla proporcionada por IBM como forma de tutorial a un blockchain de diplomas de graduados.
</br>Link de IBM  --> https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/

## Instalar y correr con docker
- Clonar repositorio </br>
$ docker-compose up --build

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

## Funcionamiento de la app


- Actualmente para usar la app de manera correcta, hay que conectarse desde la maquina que corre la app principal, en su ruta principal </br>

![](images/Annotation%202020-06-04%20003022.jpg)

Agregar algun dato al formulario, publicarlo, y clickear en minar. </br>
Lo que debe hacer que los nodos presentes en la app empiecen a calcular el nonce y publiquen en la base de datos el bloque y sus datos pertinentes. </br>

- Para verificar los hashes de los bloques minados, acceder a la ruta /chain en uno de los nodos.

## Funcionamiento del codigo

![](images/Untitled%20Diagram.png)

</br>

### Block </br>
- index: es la id del bloque </br>
- transactions: es la lista de las transacciones en el bloque </br>
- timestamp: la fecha de generacion del bloque </br>
- compute_hash(): Metodo para calcular el nonce (Numero que cambia con cada transaccion o bloque que se quiera minar, esto se hace para -añadir dificultad al generar un bloque o transaccion nueva.) </br>

### Blockchain </br>
- chain: Lista de los bloques agregados </br>
- difficulty: dificultad del nonce (Para esta app se uso un metodo de proof of work bastante sencillo, la idea es que cada hash generado deba tener cierto numero de 0 al comienzo, con este valor de dificultad, podemos aumentar o disminuir el numero de 0 necesarios.) </br>
- create_genesis_block(): crea un bloque con datos predeterminados para que el primer bloque generado oficialmente por la app pueda estar conectado a este  </br>
- last_block(): retorna la informacion del ultimo bloque añadido. </br>
- proof_of_work(): dificultad que se añade al calcular cada hash para evitar posibles alteraciones por externos al blockchain.
- add_block():revisa el proof of work y si evidentemente el bloque esta unido al anterior bloque para asi poder agregarlos a la DB.
- is_valid_proof():llamada por add_block para revisar si el proof of work es valido.
- add_new_transaction():Pila de transacciones sin minar.
- mine(): En esta funcion se hace todo el trabajo de encadenar los bloques entre si, calcular el nonce, y crear el bloque.
