print("Vamos a crear una calculadora con todas las funciones y aplicaciones. Lo primero es tomar input del usuario, así que crearemos 3 variables para primer num, \n"
      "segundo numero y el operador. Lo primero será num1 = input, junto con un prompt - enter your number -. El primer asunto es que; cuando se crea un input por el \n"
      "usuario, Python genera un string, con lo cual genera un problema para nuestra calculadora porque vamos a sumar, restar, por lo que no queremos una string. \n"
      "queremos convertir inmediatamente el input en un number-data-type. Para ello vamos a incluir la función float, con la cual rodearemos el input, de esta manera \n"
      "Inmediatamente se convertirá el input del usuario en un dato -float-. \n"
      "Luego lo otro que queremos hacer es crear el operador, ")


num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
