print("En este capitulo vamos a trabajar con listas, esto es un montónd e información. lo primero es crear la lista de datos para lo cual, necesitamos utilizar los brackets.\n"
      "los brackets le indican a python que vamos a trabajar con una lista de datos.\n"
      "Cuando creamos una variable normal en python, normalmente sólo tenemos un valor. pero cuando tenemos una lista, podemos tener varios valores dentro de una misma categoría.\n"
      "Más aún podemos entrar dentro de los valores de una misma categoría. "
      "\n (Para crear una lista debes usar los brackets cuadrados presionando \"Shift\" + la tecla de los brackets).\n"
      "Dentro de una lista puedes anotar números, o booleans(variables binarias tipo verdadero o falso)\n"
      "Una vez que tienes una lista, es MUY aprender a acceder a elementos individuales dentro de la lista. Lo primero es que siempre podemos print las listas. \n"
      "Lo segundo es que cada elemento dentro de la lista tiene un index, y el index parte en \"0\" y continua 1,2,3,4.\n"
      "Entonces para poder referirte a un elemento particular, debes escribir:\n"
      "print + el nombre de la lista + abrir corchetes redondos \"()\" + dentro abrir corchetes cuadrados\"[]\" + dentro, anotar el index.\n"
      "Si quieres elegir todos los valores a partir de un valor, como quiero todos desde el valor 1 en adelante se escribe con dos puntos despues del valor\":\" \n"
      "También podemos modificar los valores indicando el valor particular que quieres cambiar y escribiendo \"= nuevo_valor; algo así:\n "
      "\"friends[1] = Mauricio \" "
      "\"print(friends[0])\" ")
friends = ["Rafa", "Martin", "Alberto"]
friends[0] = "Mauricio"
age_of_friends = ["31", "30", "33"]
nacionalidad = ["chileno", "checo", "español"]
country = ["Chile", "Perú", "Argentina", "Colombia", "Ecuador", "Uruguay", "Paraguay", "Bolivia", "Brasil", "Panamá", "México", "Costa Rica"]
IVA_collection = ["40.2", "40.3", "26.3", "29.4", "29.8", "25.7", "36.6", "29.7", "21.1", "28.2", "23.1", "17.8"]
print("ejemplo 1")
print(friends[0])
print(country[6:])
print(friends[2]+ " tiene " + age_of_friends[2] + " años y es " + nacionalidad[2])
print("ejemplo 2")
print("ejemplo 3")
print(country[8] + " tiene una recaudación de IVA de " + IVA_collection[8] + "%.")