print("Una Función es basicamente una collección de códigos que realizan una tarea/task específica. Uno puede tomar un montón de líneas de código que hacen una cosa,\n"
      " y ponerlas dentro de una función, de manera que cuando quiera realizar la tarea de ese código, simplemente voy a invocar el código.\n"
      "Esto es muy útil porque así puedo organizar mis códigos, puedo separar mis códigos entre distintas partes que hacen distintas cosas, y son bakanes.\n"
      "Por este motivo las Funciones son una herramienta esencial en Python.\n"
      "En este ejercicio vamos a crear una función que dice -Hola- al usuario.\n"
      "Para poder escribir una función, debo utilizar una keyword llamada \"def\". Cuando Python vea la keyword -def-, inmediatamente asume que se trata de una función.\n"
      "Despues de escribir -def- hay que escribir el nombre de la función. por ejemplo; \"def say_hola() :\" o \"def sayhola() :\". Esto le dice a Python que todo lo que esté \n"
      "después de \"sayhola/say_hola, va a estar DENTRO de nuestra función y para escribir un codigo que este dentro de la función tenemos que identarlo(indent it). \n"
      "INDENTAR:https://es.wikipedia.org/wiki/Indentaci%C3%B3n . En sepañol también se dice \"sangrado\". significa mover un bloque de texto hacia la derecha \n "
      "insertando espacios o tabuladores, para así separarlo del margen izquierdo y distinguirlo mejor del texto adyacente; en el ámbito de la imprenta, \n"
      "este concepto siempre se ha denominado sangrado o sangría.\n"
      "Si al escribir def, luego no escries con sangría, esa información no se considerará dentro del código. Aquello que se considera dentro del código estará normalmente \n"
      "marcado al costado izquierdo con unas flechas. \n"
      "En este ejemplo el codigo sera simple y de una sola línea (puede ser mas complejo y tener muchas más): - print(\"Hola amigo\")."
      "\nAhora que se ha creado el código, para poder correrlo necesito \"llamar\" a la función. Sin embargo, sólo por llamar a la función no significa que esta se ejecutará \n"
      "por default/defecto. Solo se ejecuta cuando nosotros especificamos que queremos que se ejecute para lo cual debemos escribir \"sayhola()\", y recién entonces se ejecutará.\n"
      "También es importante saber que al ejecutar una función python ira primero a cumplir la priemra orden,y  luego al encontrarse con la función, ejecutará lo que está definido \n"
      " en el código -def- y luego continua con las líneas de abajo. \n"
      "Al ponerle nombre  las funciones, la práctica usual es poner la función en minúsculas y si tiene dos palabras poner un guión_bajo.\n"
      "Por otra parte, cuando escribamos funciones, probablemente querremos información adicional que sea incluida: estas se llaman parametros.\n"
      "PARAMETRO: Son piezas de información que le damos a una función, con lo cual identificamos que cuando se llama a una función, hay que recibir cierta información.\n "
      "Por ej.- def say_hola(name):- y luego agregamos: print(\"hello\" + name); de manera que podamos escribir la función: say_hola(\"Mario\"). También se pueden \n"
      "agregar más parametros como puedes ver en el ejemplo debajo.\n"
      "Finalmente destacar que hay funciones más complejas, d emanera que lo ideal y recomendable es siempre separar tus codigos entre diversas funciones. \n"
      "De esta manera cad vez que tienes un grupo de codigos que están diseñados para realizar una tarea, suele ser un buen candidate para colocar una funcion. ")

def say_hola(name, edad):
    print("Hola Amiguito " + name + " tienes " + edad)
print("línea de arriba")
say_hola("Rimao", "32")
say_hola("Kaki", "30")
say_hola("Mono", "28")
say_hola("Kristi", "29")
print("línea de abajo")