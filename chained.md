Interpreacion del codigo chained:
El codigo empieza importando 3 modulos, definiendo 4 funciones asincronicas, gracias al modulo asyncio, y luego se define el main.

La primera funcion recibe un parametro el cual va a ser el numero de tarea. Luego genera un numero aleatorio, en segundos, el cual va a ser el tiempo que la funcion permanezca dormida mientras imprime valores. Cuando despierta, sera llamada nuevamente.

La segunda funcion es parecida a la primera, con la diferencia de que esta recibe un parametro más(resultados de la primera funcion), para luego poder mostrarlos tambien

La funcion "chain" lo que hace es inicializar un cronometro para poder medir cuanto se demora en ejecutar cada una de las funciones anteriormente mencionadas y mostrar los resultados por pantalla

La funcion main lo que hace es pasar como parametro, distintos tiempos de espera a cada una de las funciones establecidas

Lo que se hace al final del codigo, es importar el modulo sys, luego llama a un metodo(random.seed())el cual sirve para poder generar un conjunto de numeros aleatorios y generar un vector con estos resultados para poder irlos pasando como argumentos a las funciones anteriormente definidas y se establece un tiempo de inicio


