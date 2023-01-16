country = ["Chile", "Perú", "Argentina", "Colombia", "Ecuador", "Uruguay", "Paraguay", "Bolivia", "Brasil", "Panamá", "México", "Costa Rica"]
IVA_collection = ["40.2", "40.3", "26.3", "29.4", "29.8", "25.7", "36.6", "29.7", "21.1", "28.2", "23.1", "17.8"]


print("Las Listas son algunas de las estructuras más importantes donde podemos guardar nuestra información. Nos permite tomar muchos valores y organizarlos y guardarlos en una estructura \n"
      "de lista. En este ejercicio, aprenderemos algunas funciones. Normalmente, las funciones nos permiten modificar listas y también conseguir información sobre las listas.\n"
      "Función 1: PRINT. ya la conocemos bien, imprime todos los valores. \n"
      "Función 2: EXTEND. Te permite tomar una lista y agregar/ anexar otra lista al final de ella. Como por ejemplo. \"country.extend(IVA_collection)\".\n"
      "De esta manera cuando imprimes la lista \"country\", también imprimes los elementos de \"IVA_collection\".\n"
      "Función 3: APPEND. Permite agregar elementos individuales a una lista. Por ejemplo, si me faltó un país puedo agregarlo con:\"country.append(República Dominicana). \n"
      "Importante tener en cuenta que append siempre va a agregar el elemento al final.  "
      "Función 4: INSERT. La función insert agrega un elemento en la posición que tú establezcas. Para esto, la función trabaja con 2 parametros; el primer paramentro es el \n"
      "Index en el cual quieres agregar el dato (esto es el número de la posición donde quiero que vaya le dato; ej \"1\" y luego escribes el elemento. por ej. un nombre.")

country.extend(IVA_collection)
country.append("República Dominicana")

revistas = ("emol","latetera")
print(revistas)
