Prueba tecnica Supermark

- Enunciado:

Un método de seguridad comúnmente utilizado por los bancos es preguntar tres
caracteres aleatorios de una contraseña. Por ejemplo, si la contraseña es 531278, el banco
puede preguntar por el 2do, 3er, y 5to, carácter; esperando que el usuario responda con la
secuencia 3-1-7.
El archivo keylog.txt contiene 50 secuencias correctas para una contraseña específica.
Dado que cada una de las secuencias está en orden de primer carácter a último carácter,
¿Cuál es la contraseña más corta para la cual todas las secuencias son correctas?

- Interpretación:

Se lee el archivo keylog.txt en el orden de listado y se crea una contraseña uniendo caracter por caracter de cada
numero excluyendo los digitos ya incluidos y los numeros que su digito inicial ya este incluido. 

Realice los procesos y endpoint en base a dicha interpretacion, en caso de algún mal entendido o ajuste necesario
estoy atento para su corrección si se permite.

- Instalacion del proyecto:

git clone https://github.com/edinbetancourt/supermark.git

- Configuracion:

python -m venv venv

./venv/scripts/activate

pip install -r requirements.txt

- Probar la APP:

python manage.py runserver

- Abrir en el navegador el swagger:

http://localhost:8000/doc/schema/swagger-ui/

- Probar los endpoint:

GET /test/v1/getpassword   -> Muestra la contraseña derivada del archivo keylog.txt

GET /test/v1/showkeys      -> Muestra el listado de cada una de las key desde el archivo

- Crear el Docker:

docker buildx build -t supermark .

- Iniciar el Docker:

docker run -p 8000:80 -td supermark

- Abrir en el navegador el swagger:

http://localhost:8000/doc/schema/swagger-ui/


Fin.




