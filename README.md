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
