print("Comparisons; anteriormente utilizamos booleans. Hoy vamos a revisar por medio el analisis por medio de comparaciones entre distintos números, strings, y etc.\n"
      "con el resultado de las comparaciones podemos llegar a resultados. Para este tutorial crearemos una función, con la cual nos dará el número máximo que pongamos \n"
      "en ella. Así, esta función tomara como input 3 parametros e imprimirá el mayor numero que ingresemos.\n"
      "Las COMPARACIONES a diferencia de BOOLEANS, no se determinan por Verdadero o Falso si no que contrastan distintos valores; y por eso se utilizan los criterios -\n"
      " \"Igual, mayor o menor que\"o los llamados \"Comparison Operator\": =; ==; <; >; <=; >=. \n"
      "Ahora crearemos una funcion que seleccione el mayor valor: primero comprobamos si num1 es el amyor, luego si es que es num2, y si ninguno de los anteriores califica \n"
      "Entonces necesariamente será num3.")

def max_num(num1, num2, num3):
    if  num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
