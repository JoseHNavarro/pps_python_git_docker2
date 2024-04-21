# pps_python_git_docker2

Bienvenido! Este proyecto es algo parecido a las galletas de la fortuna, en las que tu das a un boton y te aparecerá una frase auspiciosa

Para crear el entorno virtual: `python -m venv nombre_entorno`
para activarlo ejecutamos el siguiente comando: `source nombre_entorno/bin/activate`

para resolver dependencias `pip install -r requirements.txt`

Si queremos iniciar la aplicación, ejecutamos el comando `flask run`
tras esto, en el terminal nos saldra una url, copiamos y la pegamos en el navegador

DOCKER

Bien, para Docker necesitamos seguir los siguientes pasos

Lo primero es crear la imagen con `docker build -t nombreimagen .`

Con la imagen creada, hay que crear el contenedor, ejecutando `docker run -p port:5000`. Importante decir que el puerto has de elegirlo tú.

A partir de aqui, el proceso es igual que antes: en el terminal nos saldrá el enlace a la web, copiamos y pegamos y ya estaría. Si todo ha ido bien, deberías ver el "Hola, mundo!", y al escribir en la URL "/frotar/numero", donde numero es un numero que tu quieras, nos saldrán varias frases tantas veces como hayas escrito


MONGO
Lo primero es levantar un contenedor con la imagen de mongoDB `docker run -d --name nombre -p 27017:27017 mongo`
Nos metemos en nuestro entorno virtual y instalamos las dependencias descritas en requirements.txt
Asegúrate de tener instalados tanto Docker como Mongodb. Tras comprobarlo podemos ejecutar el siguiente comando:` docker network create nombre`
Con esto estableces la conexión entre la app y mongo
Ejecutamos `docker network connect nombreRed nombreImagen`

Ahora creamos la imagen de la app
`docker build -t nombre .`

Y ya para desplegar un contenedor con la imagen que has creado, ejecuta el comando `docker run -p port:5000 --network nombreRed nombreImagen`
Asi asocias el contenedor de la imagen que has creado a un puerto y una red que hayas especificado
