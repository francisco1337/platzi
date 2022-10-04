#############################################################
########## CLASES PREDEFINIDAS Y CONSTRUIDAS#################
#############################################################

. = Busca un caracter sin importar cual
\d = Busca un digito sin importar cual
\d = Busca un caracter numero o texto sin importar cual
\s = busca espacios en blancos
\n = busca saltos de linea
[0-9] = busca numeros del 0 al 9 y es una manera mas estricta
[a-zA-Z0-9_] = Busca texto numeros y guion bajo
\. = busca el caracter punto .
\d* = encuentra ninguno uno o todos los caracteres (busca un digito y encuentra todo lo demas)
\d+ = encuentra uno o mas los caracteres (busca un digito y encuentra todo lo demas)
\d*[a-z] = encuentra ninguno, uno o varios digitos y letras
? = cero o uno
\d{4,10} = cantidad de digitos minimos a maximos
[] = busca lo contenido dentro en la misma posicion
^ =  NEGACION al principio del elemento
^\[LOG.*\[LOG\].*$ = Busqueda de archivos log
^\[LOG.*\[LOG\].*user:@celismx\] .*$ = Busqueda de archivos log

#############################################################
########## CLASES PREDEFINIDAS Y CONSTRUIDAS COPIA ##########
#############################################################
\t — Representa un tabulador.
\r — Representa el “retorno de carro” o “regreso al inicio” o sea el lugar en que la línea vuelve a iniciar.
\n — Representa la “nueva línea” el carácter por medio del cual una línea da inicio. Es necesario recordar que en Windows es necesaria una combinación de \r\n para comenzar una nueva línea, mientras que en Unix solamente se usa \n y en Mac_OS clásico se usa solamente \r.
\a — Representa una “campana” o “beep” que se produce al imprimir este carácter.
\e — Representa la tecla “Esc” o “Escape”
\f — Representa un salto de página
\v — Representa un tabulador vertical
\x — Se utiliza para representar caracteres ASCII o ANSI si conoce su código. De esta forma, si se busca el símbolo de derechos de autor y la fuente en la que se busca utiliza el conjunto de caracteres Latin-1 es posible encontrarlo utilizando “\xA9”.
\u — Se utiliza para representar caracteres Unicode si se conoce su código. “\u00A2” representa el símbolo de centavos. No todos los motores de Expresiones Regulares soportan Unicode. El .Net Framework lo hace, pero el EditPad Pro no, por ejemplo.
\d — Representa un dígito del 0 al 9.
\w — Representa cualquier carácter alfanumérico.
\s — Representa un espacio en blanco.
\D — Representa cualquier carácter que no sea un dígito del 0 al 9.
\W — Representa cualquier carácter no alfanumérico.
\S — Representa cualquier carácter que no sea un espacio en blanco.
\A — Representa el inicio de la cadena. No un carácter sino una posición.
\Z — Representa el final de la cadena. No un carácter sino una posición.
\b — Marca la posición de una palabra limitada por espacios en blanco, puntuación o el inicio/final de una cadena.
\B — Marca la posición entre dos caracteres alfanuméricos o dos no-alfanuméricos.


