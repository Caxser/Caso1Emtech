from lifestore_file import lifestore_products, lifestore_searches, lifestore_sales

#inicializando listas necesarias
lista_venta = []
lista_contada = []
in_contado = []
a=lifestore_products

#acceso a usuario
usuarios_lista= [["admin", "12345"],["1","1"]]

print(""" 
                      ¡Bienvenido!

Inicie sesión para utilizar el programa

                'Usuario prueba: admin
                'contraseña prueba: 12345
""")

usuario_log= input("Ingrese su usuario: ")
contrasena= input("Ingrese su contraseña: ")
intentos=0
acceso=0
while intentos<3 and acceso==0:
  for usuario in usuarios_lista:
    if usuario[0]== usuario_log and intentos<3: 
      if usuario[1]== contrasena:
        print("")
        print("")
        print("Usuario activo: ", usuario_log)
        acceso= 1
        break
      else:
        
    
        if intentos<3 and acceso==0:
          print("""
    Usuario o contraseña invalidos
    
    Verifique e intente de nuevo

          """)
          print("Intentos restantes: ", 3-intentos)
          usuario_log= input("Ingrese su usuario: ")
          contrasena= input("Ingrese su contraseña: ")
          intentos+=1
          break
          
  if intentos<3 and acceso==0:
          print("""
    Usuario o contraseña invalidos
    
    Verifique e intente de nuevo

          """)
          print("Intentos restantes: ", 3-intentos)
          usuario_log= input("Ingrese su usuario: ")
          contrasena= input("Ingrese su contraseña: ")
          intentos+=1
    
  
#da acceso al análisis de datos solo si se paso autenticacion
if acceso== 1:
  
#primer paso, obtener indices de cada venta, para despues contarlas
  for elemento in lifestore_sales:
    #if me sirve para filtrar los productos devueltos, ya que no cuentan como ventas
      if elemento[4] == 0:
        #elemento[1] nos devuelve el valor de la primera posición, en este caso indice
          indice = elemento[1]
        #añadimos el indice a la lista de venta
          lista_venta.append(indice)

#
#
#_______________________

#contabilizar cada indice sin repetirlo
  for i in lista_venta:
    # i es cada elemento en nuestra lista de venta
      indice = i
    #se pasa un filtro, para evitar repetición
      if i not in in_contado:
        #se usa la función count para contar cada indice en la lista
          cuenta = lista_venta.count(indice)
        #se añade en una multilista, tanto indice como la cuenta
          lista_contada.append([indice, cuenta])
        #además, se añade el indice para hacer funcionar el filtro
          in_contado.append(indice)
#regresa lista_contada[indice producto, cantidad]

#_________________
#ordenar de mayor a menor
  ventas_mayor = []
  while lista_contada:
    maximo = lista_contada[0][1]
    lista_actual = lista_contada[0]
    for venta_producto in lista_contada:
        if venta_producto[1] > maximo:
            maximo = venta_producto[1]
            lista_actual = venta_producto
    ventas_mayor.append(lista_actual)
    lista_contada.remove(lista_actual)

#lista creada ventas_mayor[indice,numero de ventas]
#copia de seguridad de ventas mayor
  copia_ventas_mayor= ventas_mayor[:]


#_____________________
#top mejores busquedas
  top_busqueda = []
  in_contado = []
  busquedas = []

  for elemento in lifestore_searches:
    #elemento[1] nos devuelve el valor de la primera posición, en este caso indice
    indice = elemento[1]
    #añadimos el indice a la lista de venta
    busquedas.append(indice)

#contabilizar cada indice sin repetirlo
  for i in busquedas:
    # i es cada elemento en nuestra lista de venta
    indice = i
    #se pasa un filtro, para evitar repetición
    if i not in in_contado:
        #se usa la función count para contar cada indice en la lista
        cuenta = busquedas.count(indice)
        #se añade en una multilista, tanto indice como la cuenta
        top_busqueda.append([indice, cuenta])
        #además, se añade el indice para hacer funcionar el filtro
        in_contado.append(indice)
#regresa la lista top_busqueda
#

#_________________
#ordenar de mayor a menor
  top_busqueda_mayor = []
  while top_busqueda:
    maximo = top_busqueda[0][1]
    lista_actual = top_busqueda[0]
    for busqueda in top_busqueda:
        if busqueda[1] > maximo:
            maximo = busqueda[1]
            lista_actual = busqueda
    top_busqueda_mayor.append(lista_actual)
    top_busqueda.remove(lista_actual)
#lista creada top_busqueda_mayor

#_________________________
#Reseña

  resenas = []
  for elemento in lifestore_sales:
    #atrapa el id y el score, añadiendolos a una nueva lista
    id_prod = elemento[1]
    score = elemento[2]
    resenas.append([id_prod, score])
#lista resenas
#print(resenas)
#para contarlas y sumarlas, se crea filtro y nueva lista
  resenas_contadas = []
  filtro = []
  for resena in resenas:
    #inicializa contador y valor
    producto = resena[0]
    contador = 1
    suma = resena[1]
    #print(elemento)
    if producto not in filtro:
        #se compara cada elemento de la lista, si no esta en el filtro
        for i in resenas:
            #print(i)
            if producto == i[0]:
                #solo los elementos iguales se suman y cuentan
                suma += i[1]
                contador += 1
                
        res_prom = suma / contador
        #
        resenas_contadas.append([producto, round(res_prom, 1)])
        filtro.append(producto)

#lista resenas_contadas[id producto, resena prom]

#_________________________________________________
#ordenar de mayor a menor
  top_resena_mayor = []
  while resenas_contadas:
    maximo = resenas_contadas[0][1]
    lista_actual = resenas_contadas[0]
    for busqueda in resenas_contadas:
        if busqueda[1] > maximo:
            maximo = busqueda[1]
            lista_actual = busqueda
    top_resena_mayor.append(lista_actual)
    resenas_contadas.remove(lista_actual)
#lista creada top_resena_mayor[id producto, resena prom]


#sacar categorias
  categoria_resena = []
  productos_copia = []
  for producto in lifestore_products:
    productos_copia.append(producto[3])

  categorias = []
  for producto in productos_copia:
    categoria = producto
    if categoria not in categorias:
        categorias.append(categoria)
        productos_copia.remove(producto)
    else:
        productos_copia.remove(producto)
#lista de categorias
#_______________
#construcción menú:
  opcion=0
  while opcion==0:
    print(""" 
    Escriba el numero de la opción que requiera

    1) Listado de productos con más ventas
    2) Listado de productos con menos ventas
    3) Listado de productos con más busquedas
    4) Listado de productos con menos busquedas
    5) Listado de productos con mejores reseñas
    6) Listado de productos con peores reseñas
    7) Total de ventas
    8) Salir del programa
  """)
    opcion= input("Ingrese su selección: ")
# 8 rompe todo y finaliza
    if opcion== "8":
      break




#opción 1 resultados
    while opcion== "1" and acceso==1:
      print(""" 
              Productos más vendidos

Seleccione una de las siguientes opciones:
    1) Listado con todas las categorias incluidas
    2) Listado por categoria
    3) Menu anterior

      """)
      opcion_1= input("Teclee su respuesta y presione enter: ")
      if opcion_1=="1" and acceso==1:
        #lista ventas_mayor[indice,numero de ventas]
        print(""" 
              Lista con los 20 productos mejor vendidos
        """)
        lista_top_ventas=[]
        ventas_top_20= ventas_mayor[0:20]
        numeral=1
        
        while numeral<=20:
          for producto_ven in ventas_top_20:
          
            for producto in lifestore_products:
              if producto_ven[0] == producto[0]:
                print(numeral, ".- ", producto[1], " total ventas: ", producto_ven[1])
                numeral += 1
                ventas_top_20.remove(producto_ven)
                break
        print("""
      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa
            """)
        cambio_op=input("Respuesta: ")
        if cambio_op == "a" :
          continue
        elif cambio_op == "b" :
          break
        else:
          no_op=0
          while no_op==0:
            print("Opción no valida, intente nuevamente")
            print("""

      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa

            """)
            cambio_op=input("Respuesta: ")
            if cambio_op == "a" :
              no_op=1
              continue
            elif cambio_op == "b" :
              acceso=0
              no_op=1
              break
              



      #inicia subopcion 2_________________________________
      if opcion_1=="2":
        while opcion_1=="2":
        #categorias productos
          print("""
              Productos más vendidos

Si quiere ver el top 10 de productos más buscados, en las categorias a continuación
""")
          print("Total de categorias: ", len(categorias))
          numeral = 1
          for categoria in categorias:

            print(numeral, ".- ", categoria)
            numeral += 1
          intentos = 0
      
          busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
  """)
          valor="bien"
          try:
            busqueda = int(busqueda)
          except (ValueError):
            valor = "mal"

        
          if valor =="mal" and intentos<= 3:
            print("El valor ingresado no corresponde a alguna de las opciones")
            print("intente de nuevo")
            busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
            """)
            intentos += 1
            if intentos == 4:
              print("Intentos excedidos, reiniciando programa")
              acceso=0
            print("Intentos restantes: ", 4 - intentos)
     
          if acceso==1: 
            busqueda = int(busqueda)
            if busqueda == 0 or busqueda > len(categorias):
              print("""
    La opción que ha escogido es invalida.
      Verifique e intente nuevamente.
        """)

              intentos += 1
              if intentos == 4:
                print("Intentos excedidos, reiniciando programa")
                acceso=0
                break
              print("Intentos restantes: ", 4 - intentos)
            
              continue
            else:
              busqueda = int(busqueda)
        
  #si usuario excede intentos, rompe ciclo
      
      
          if acceso==1:
            busqueda = categorias[busqueda-1]
#_______________________________________________-
#Comienza definición del top

        
            productos_copia = a

            lista_productos_req = []
            for producto in productos_copia:
              if producto[3] == busqueda:
                lista_productos_req.append(producto[0])
              else:
                continue
      #lista ordenada por ventas
      #lista ventas_mayor[indice,numero de ventas]
        
            ventas_cat_top=ventas_mayor[:]
            numeral=1
            prod_cat_venta = []
            print("Lista con mejores venta de la categoria ", busqueda)
        
            for venta in ventas_cat_top:
              if numeral<=20:
                for prod_cat in lista_productos_req:
                    if prod_cat == venta[0]:
                      for producto in lifestore_products:
                      
                        if venta[0]== producto[0]:
                    
                          print(numeral,".- ", producto[1], " con un total de ventas de: ", venta[1])
                          numeral+=1

                          break
          print("""
      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) Salir del programa
            """)
          cambio_op=input("Respuesta: ")
          if cambio_op == "a" :
            opcion_1="2"
          elif cambio_op == "b" :
            break
          elif cambio_op == "c":
            acceso=0
            break
          else:
            no_op=0
            while no_op==0:
              print("Opción no valida, intente nuevamente")
              print("""

      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa

            """)
              cambio_op=input("Respuesta: ")
              if cambio_op == "a" :
                no_op=1
                continue
              elif cambio_op == "b" :
                acceso=0
                no_op=1
                break

      if opcion_1== "3":
        opcion=0





#opción 2 menu general    
    while opcion=="2" and acceso==1:
      print(""" 
              Productos menos vendidos

Seleccione una de las siguientes opciones:
    1) Listado con todas las categorias incluidas
    2) Listado por categoria
    3) Menu anterior

      """)
      opcion_2= input("Teclee su respuesta y presione enter: ")
      if opcion_2=="1" and acceso==1:
        #lista ventas_mayor[indice,numero de ventas]
        
        print(""" 
              Lista con los 20 productos con menores ventas
        """)
        lista_top_ventas=[]

        ventas_menor= ventas_mayor[:]
        ventas_menor.reverse()
        
        ventas_top_20= ventas_menor[0:20]
        numeral=1
        
        while numeral<=20:
          for producto_ven in ventas_top_20:
          
            for producto in lifestore_products:
              if producto_ven[0] == producto[0]:
                print(numeral, ".- ", producto[1], " total ventas: ", producto_ven[1])
                numeral += 1
                ventas_top_20.remove(producto_ven)
                break
        #necesitamos añadir productos que no figuran en ventas, o mejor dicho que no se vendieron
        print("""
                        Productos no vendidos
                      
        """)
        numeral=1
        productos_no_ven= lifestore_products[:]

        
        for producto in ventas_menor:
            
            for producto_ven in productos_no_ven:
              if producto_ven[0] == producto[0]:
                
                productos_no_ven.remove(producto_ven)
                break
        print("No fueron vendidos un total de: ", len(productos_no_ven)," productos")
        print("A continuación se muestran algunos de ellos(20)")        
        
        for producto_no_vendido in productos_no_ven:
          if numeral<=20:  
            print(numeral, ".- ", producto_no_vendido[1], " Sin ventas")
            numeral += 1

        print("""
      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa
            """)
        cambio_op=input("Respuesta: ")
        if cambio_op == "a" :
          continue
        elif cambio_op == "b" :
          break
        else:
          no_op=0
          while no_op==0:
            print("Opción no valida, intente nuevamente")
            print("""

      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa

            """)
            cambio_op=input("Respuesta: ")
            if cambio_op == "a" :
              no_op=1
              continue
            elif cambio_op == "b" :
              acceso=0
              no_op=1
              break
              



      #inicia subopcion 2_________________________________
      if opcion_2=="2" and acceso==1:
        while opcion_2=="2" and acceso==1:
        #categorias productos
          print("""
              Productos menos vendidos

Si quiere ver el top 10 de productos menos vendidos, dentro de cada una de las categorias a continuación
""")
          print("Total de categorias: ", len(categorias))
          numeral = 1
          for categoria in categorias:

            print(numeral, ".- ", categoria)
            numeral += 1
          intentos = 0
      
          busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
  """)
          valor="bien"
          try:
            busqueda = int(busqueda)
          except (ValueError):
            valor = "mal"

        
            while valor =="mal":
              print("El valor ingresado no corresponde a alguna de las opciones")
              print("Intente de nuevo")
              busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
            """)
              intentos += 1
              if intentos == 4:
                print("Intentos excedidos")
                valor="cero"
                acceso=0
                break
              print("Intentos restantes: ", 4 - intentos)
     
          if acceso==1: 
            busqueda = int(busqueda)
            if busqueda == 0 or busqueda > len(categorias):
              print("""
    La opción que ha escogido es invalida.
      Verifique e intente nuevamente.
        """)

              intentos += 1
              #bucle inactivo
              if intentos == 4:
                print("Intentos excedidos, reiniciando programa")
                acceso=0
                break
              #print("Intentos restantes: ", 4 - intentos)
              
              continue
            else:
              busqueda = int(busqueda)
        
  #si usuario excede intentos, rompe ciclo
      
      
          if acceso==1:
            busqueda = categorias[busqueda-1]
  #_______________________________________________-
  #Comienza definición del top

        
            productos_copia = a

            lista_productos_req = []
            for producto in productos_copia:
              if producto[3] == busqueda:
                lista_productos_req.append(producto[0])
              else:
                continue
      #lista ordenada por ventas
      #lista ventas_menor[indice,numero de ventas]
            ventas_menor= ventas_mayor[:]
            ventas_menor.reverse()

            ventas_cat_top=ventas_menor[:]
            numeral=1
            prod_cat_venta = []
            
            print("""
            
            """)
            print("Lista con productos menos vendidos de la categoria ", busqueda)
            
            for venta in ventas_cat_top:
              if numeral<=20:
                for prod_cat in lista_productos_req:
                    if prod_cat == venta[0]:
                      for producto in lifestore_products:
                      
                        if venta[0]== producto[0]:
                    
                          print(numeral,".- ", producto[1], " con un total de ventas de: ", venta[1])
                          lista_productos_req.remove(prod_cat)
                          numeral+=1

                          break
            #necesario revisar articulos que no fueron vendidos
            numeral=1
            
            if len(lista_productos_req) > 0:
              print(""" 
                  Existen productos no vendidos
                   Se enlistan a continuación
              """)
              print("Total no vendidos: ", len(lista_productos_req), ", se enlistan solo 10")
              
              for prod_cat in lifestore_products:
                for producto in lista_productos_req:
                  if numeral<=10:
                    if producto== prod_cat[0]:
                      print(numeral, ".- ", prod_cat[1])
                      numeral+=1
                      lista_productos_req.remove(producto)
                      break
              

          if acceso==1:
            print("""
      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) Salir del programa
            """)
            cambio_op=input("Respuesta: ")
            if cambio_op == "a" :
              opcion_2="2"
            elif cambio_op == "b" :
              break
            elif cambio_op == "c":
              acceso=0
              break
            else:
              no_op=0
              while no_op==0:
                print("Opción no valida, intente nuevamente")
                print("""

      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa

            """)
                cambio_op=input("Respuesta: ")
                if cambio_op == "a" :
                  no_op=1
                  continue
                elif cambio_op == "b" :
                  acceso=0
                  no_op=1
                  break

      if opcion_2== "3" and acceso==1:
        opcion=0
#Fin seccion menos ventas






#si la opción se matiene se vuelve infinito, sección de busquedas
    while opcion== "3" and acceso==1:
      print(""" 
              Productos más buscados

Seleccione una de las siguientes opciones:
    1) Listado con todas las categorias incluidas
    2) Listado por categoria
    3) Menu anterior

      """)
      opcion_3= input("Teclee su respuesta y presione enter: ")
      if opcion_3=="1" and acceso==1:
        #lista ventas_mayor[indice,numero de ventas]
        print(""" 
              Lista con los 20 productos más buscados
        """)
        lista_top_busqueda=[]
        busqueda_top_20= top_busqueda_mayor[0:20]
        numeral=1
        
        
        while numeral<=20:
          for producto_bus in busqueda_top_20:
          
            for producto in lifestore_products:
              if producto_bus[0] == producto[0]:
                print(numeral, ".- ", producto[1], " total busquedas: ", producto_bus[1])
                numeral += 1
                busqueda_top_20.remove(producto_bus)
                break
        print("""
      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa
            """)
        cambio_op=input("Respuesta: ")
        if cambio_op == "a" :
          continue
        elif cambio_op == "b" :
          break
        else:
          no_op=0
          while no_op==0:
            print("Opción no valida, intente nuevamente")
            print("""

      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa

            """)
            cambio_op=input("Respuesta: ")
            if cambio_op == "a" :
              no_op=1
              continue
            elif cambio_op == "b" :
              acceso=0
              no_op=1
              break
              



      #inicia subopcion 2_________________________________
      if opcion_3=="2":
        while opcion_3=="2":
        #categorias productos
          print("""
              Productos más buscados

Si quiere ver el top 10 de productos más buscados, en las categorias a continuación
""")
          print("Total de categorias: ", len(categorias))
          numeral = 1
          for categoria in categorias:

            print(numeral, ".- ", categoria)
            numeral += 1
          intentos = 0
      
          busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
  """)
          valor="bien"
          try:
            busqueda = int(busqueda)
          except (ValueError):
            valor = "mal"

        
          if valor =="mal" and intentos<= 3:
            print("El valor ingresado no corresponde a alguna de las opciones")
            print("intente de nuevo")
            busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
            """)
            intentos += 1
            if intentos == 4:
              print("Intentos excedidos, reiniciando programa")
              acceso=0
            print("Intentos restantes: ", 4 - intentos)
     
          if acceso==1: 
            busqueda = int(busqueda)
            if busqueda == 0 or busqueda > len(categorias):
              print("""
    La opción que ha escogido es invalida.
      Verifique e intente nuevamente.
        """)

              intentos += 1
              #bucle deshabilitado
              if intentos == 4:
                print("Intentos excedidos, reiniciando programa")
                acceso=0
                break
              #print("Intentos restantes: ", 4 - intentos)
            
              continue
            else:
              busqueda = int(busqueda)
        
  #si usuario excede intentos, rompe ciclo
      

          if acceso==1:
            busqueda = categorias[busqueda-1]
#_______________________________________________-
#Comienza definición del top

        
            productos_copia = a

            lista_productos_req = []
            for producto in productos_copia:
              if producto[3] == busqueda:
                lista_productos_req.append(producto[0])
              else:
                continue
      #lista ordenada por ventas
      #lista top_busqueda_mayor[indice,numero de ventas]
        
            busqueda_cat_top=top_busqueda_mayor[:]
            numeral=1
            prod_cat_venta = []
            print("Lista con mejores busquedas de la categoria ", busqueda)
        
            for busqueda in busqueda_cat_top:
              if numeral<=20:
                for prod_cat in lista_productos_req:
                    if prod_cat == busqueda[0]:
                      for producto in lifestore_products:
                      
                        if busqueda[0]== producto[0]:
                    
                          print(numeral,".- ", producto[1], " con un total de busquedas de: ", busqueda[1])
                          numeral+=1

                          break
          print("""
      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) Salir del programa
            """)
          cambio_op=input("Respuesta: ")
          regresar_menu=0
          if cambio_op == "a" :
            opcion_3="2"
          elif cambio_op == "b" :
            break
          elif cambio_op == "c":
            acceso=0
            break
          else:
            no_op=0
            while no_op==0:
              print("Opción no valida, intente nuevamente")
              print("""

      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) salir del programa

            """)
              cambio_op=input("Respuesta: ")
              if cambio_op == "a" :
                no_op=1
                continue
              elif cambio_op=="b":
                no_op=1
                regresar_menu=1
                break
              elif cambio_op == "c" :
                acceso=0
                no_op=1
                break
          if regresar_menu== 1:
            break

      if opcion_3== "3":
        opcion=0
  





#listado de productos con menos busquedas
    while opcion=="4" and acceso==1:
      
      print(""" 
              Productos menos buscados

Seleccione una de las siguientes opciones:
    1) Listado con todas las categorias incluidas
    2) Listado por categoria
    3) Menu anterior

      """)
      opcion_4= input("Teclee su respuesta y presione enter: ")
      if opcion_4=="1" and acceso==1:
        #lista ventas_mayor[indice,numero de ventas]
        print(""" 
              Lista con los 20 productos menos buscados
        """)
        lista_top_busqueda=[]
        busqueda_menor= top_busqueda_mayor[:]
        busqueda_menor.reverse()
        busqueda_top_20= busqueda_menor[0:20]
        
        numeral=1
        
        
        while numeral<=20:
          for producto_bus in busqueda_top_20:
          
            for producto in lifestore_products:
              if producto_bus[0] == producto[0]:
                print(numeral, ".- ", producto[1], " total busquedas: ", producto_bus[1])
                numeral += 1
                busqueda_top_20.remove(producto_bus)
                break
        #necesitamos añadir productos que no figuran en ventas, o mejor dicho que no se vendieron
        print("""
                        Productos sin busquedas
                      
        """)
        numeral=1
        productos_no_bus= lifestore_products[:]

        
        for producto in busqueda_menor:
            
            for producto_bus in productos_no_bus:
              if producto_bus[0] == producto[0]:
                
                productos_no_bus.remove(producto_bus)
                break
        print("No fueron buscados un total de: ", len(productos_no_bus)," productos")
        print("A continuación se muestran algunos de ellos(20)")        
        
        for producto_no_buscado in productos_no_bus:
          if numeral<=20:  
            print(numeral, ".- ", producto_no_buscado[1], " Sin busquedas")
            numeral += 1
        print("""
      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa
            """)
        cambio_op=input("Respuesta: ")
        if cambio_op == "a" :
          continue
        elif cambio_op == "b" :
          break
        else:
          no_op=0
          while no_op==0:
            print("Opción no valida, intente nuevamente")
            print("""

      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa

            """)
            cambio_op=input("Respuesta: ")
            if cambio_op == "a" :
              no_op=1
              continue
            elif cambio_op == "b" :
              acceso=0
              no_op=1
              break
              



#inicia subopcion 2_________________________________
      if opcion_4=="2":
        while opcion_4=="2":
        #categorias productos
          print("""
              Productos menos buscados

Si quiere ver el top 10 de productos menos buscados, en las categorias a continuación
""")
          print("Total de categorias: ", len(categorias))
          numeral = 1
          for categoria in categorias:

            print(numeral, ".- ", categoria)
            numeral += 1
          intentos = 0
      
          busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
  """)
          valor="bien"
          try:
            busqueda = int(busqueda)
          except (ValueError):
            valor = "mal"

        
          if valor =="mal" and intentos<= 3:
            print("El valor ingresado no corresponde a alguna de las opciones")
            print("intente de nuevo")
            busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
            """)
            intentos += 1
            if intentos == 4:
              print("Intentos excedidos, reiniciando programa")
              acceso=0
            print("Intentos restantes: ", 4 - intentos)
     
          if acceso==1: 
            busqueda = int(busqueda)
            if busqueda == 0 or busqueda > len(categorias):
              print("""
    La opción que ha escogido es invalida.
      Verifique e intente nuevamente.
        """)

              intentos += 1
              #bucle deshabilitado
              if intentos == 4:
                print("Intentos excedidos, reiniciando programa")
                acceso=0
                break
              #print("Intentos restantes: ", 4 - intentos)
            
              continue
            else:
              busqueda = int(busqueda)
        
      

          if acceso==1:
            busqueda = categorias[busqueda-1]
#_______________________________________________-
#Comienza definición del top

        
            productos_copia = a

            lista_productos_req = []
            for producto in productos_copia:
              if producto[3] == busqueda:
                lista_productos_req.append(producto[0])
              else:
                continue
      #lista ordenada por ventas
      #lista top_busqueda_mayor[indice,numero de ventas]
        
            busqueda_menor= top_busqueda_mayor[:]
            busqueda_menor.reverse()
            busqueda_cat_top=busqueda_menor[:]
            numeral=1
            prod_cat_venta = []
            print("Lista con productos menos buscados de la categoria ", busqueda)
        
            for busqueda in busqueda_cat_top:
              if numeral<=20:
                for prod_cat in lista_productos_req:
                    if prod_cat == busqueda[0]:
                      for producto in lifestore_products:
                      
                        if busqueda[0]== producto[0]:
                    
                          print(numeral,".- ", producto[1], " con un total de busquedas de: ", busqueda[1])
                          lista_productos_req.remove(prod_cat)
                          numeral+=1

                          break
          #necesario revisar articulos que no fueron vendidos
            numeral=1
            
            if len(lista_productos_req) > 0:
              print(""" 
                  Existen productos no buscados
                   Se enlistan a continuación
              """)
              print("Total no buscados: ", len(lista_productos_req), ", se enlistan solo 10")
              
              for prod_cat in lifestore_products:
                for producto in lista_productos_req:
                  if numeral<=10:
                    if producto== prod_cat[0]:
                      print(numeral, ".- ", prod_cat[1])
                      numeral+=1
                      lista_productos_req.remove(producto)
                      break
 
          print("""
      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) Salir del programa
            """)
          cambio_op=input("Respuesta: ")
          regresar_menu=0
          if cambio_op == "a" :
            opcion_4="2"
          elif cambio_op == "b" :
            break
          elif cambio_op == "c":
            acceso=0
            break
          else:
            no_op=0
            while no_op==0:
              print("Opción no valida, intente nuevamente")
              print("""

      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) salir del programa

            """)
              cambio_op=input("Respuesta: ")
              if cambio_op == "a" :
                no_op=1
                continue
              elif cambio_op=="b":
                no_op=1
                regresar_menu=1
                break
              elif cambio_op == "c" :
                acceso=0
                no_op=1
                break
          if regresar_menu== 1:
            break

      if opcion_4== "3":
        opcion=0
    




#opcion 5 menu general
    while opcion=="5" and acceso==1:
      
      print(""" 
              Productos con mejores reseñas

Seleccione una de las siguientes opciones:
    1) Listado con todas las categorias incluidas
    2) Listado por categoria
    3) Menu anterior

      """)
      opcion_5= input("Teclee su respuesta y presione enter: ")
      if opcion_5=="1" and acceso==1:
        #lista top_resena_mayor[id producto, resena prom]
        print(""" 
              Lista con los 20 productos con mejor reseña
        """)
        lista_top_busqueda=[]
        resena_top_20= top_resena_mayor[0:20]
        numeral=1
        
        
        while numeral<=20:
          for producto_bus in resena_top_20:
          
            for producto in lifestore_products:
              if producto_bus[0] == producto[0]:
                print(numeral, ".- ", producto[1], " calificación promedio: ", producto_bus[1])
                numeral += 1
                resena_top_20.remove(producto_bus)
                break
        print("""
      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa
            """)
        cambio_op=input("Respuesta: ")
        if cambio_op == "a" :
          continue
        elif cambio_op == "b" :
          break
        else:
          no_op=0
          while no_op==0:
            print("Opción no valida, intente nuevamente")
            print("""

      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa

            """)
            cambio_op=input("Respuesta: ")
            if cambio_op == "a" :
              no_op=1
              continue
            elif cambio_op == "b" :
              acceso=0
              no_op=1
              break
              



      #inicia subopcion 2_________________________________
      if opcion_5=="2":
        while opcion_5=="2":
        #categorias productos
          print("""
              Productos con mejores reseñas

Si quiere ver el top 10 de productos con mejor reseña, en las categorias a continuación
""")
          print("Total de categorias: ", len(categorias))
          numeral = 1
          for categoria in categorias:

            print(numeral, ".- ", categoria)
            numeral += 1
          intentos = 0
      
          busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
  """)
          valor="bien"
          try:
            busqueda = int(busqueda)
          except (ValueError):
            valor = "mal"

        
          if valor =="mal" and intentos<= 3:
            print("El valor ingresado no corresponde a alguna de las opciones")
            print("intente de nuevo")
            busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
            """)
            intentos += 1
            if intentos == 4:
              print("Intentos excedidos, reiniciando programa")
              acceso=0
            print("Intentos restantes: ", 4 - intentos)
     
          if acceso==1: 
            busqueda = int(busqueda)
            if busqueda == 0 or busqueda > len(categorias):
              print("""
    La opción que ha escogido es invalida.
      Verifique e intente nuevamente.
        """)

              intentos += 1
              #bucle deshabilitado
              if intentos == 4:
                print("Intentos excedidos, reiniciando programa")
                acceso=0
                break
              #print("Intentos restantes: ", 4 - intentos)
            
              continue
            else:
              busqueda = int(busqueda)
        
  #si usuario excede intentos, rompe ciclo
      

          if acceso==1:
            busqueda = categorias[busqueda-1]
#_______________________________________________-
#Comienza definición del top

        
            productos_copia = a

            lista_productos_req = []
            for producto in productos_copia:
              if producto[3] == busqueda:
                lista_productos_req.append(producto[0])
              else:
                continue
      #lista ordenada
      #lista top_resena_mayor[id producto, resena prom]
        
            resena_cat_top=top_resena_mayor[:]
            numeral=1
            prod_cat_venta = []
            print("Lista con mejores reseñas de la categoria ", busqueda)
        
            for resena in resena_cat_top:
              if numeral<=20:
                for prod_cat in lista_productos_req:
                    if prod_cat == resena[0]:
                      for producto in lifestore_products:
                      
                        if resena[0]== producto[0]:
                    
                          print(numeral,".- ", producto[1], " calificación promedio: ", resena[1])
                          numeral+=1

                          break
          print("""
      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) Salir del programa
            """)
          cambio_op=input("Respuesta: ")
          regresar_menu=0
          if cambio_op == "a" :
            opcion_5="2"
          elif cambio_op == "b" :
            break
          elif cambio_op == "c":
            acceso=0
            break
          else:
            no_op=0
            while no_op==0:
              print("Opción no valida, intente nuevamente")
              print("""

      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) salir del programa

            """)
              cambio_op=input("Respuesta: ")
              if cambio_op == "a" :
                no_op=1
                continue
              elif cambio_op=="b":
                no_op=1
                regresar_menu=1
                break
              elif cambio_op == "c" :
                acceso=0
                no_op=1
                break
          if regresar_menu== 1:
            break

      if opcion_5== "3":
        opcion=0





#Opcion 6 menu general
    while opcion=="6" and acceso==1:
      
      print(""" 
              Productos con la peores reseñas

Seleccione una de las siguientes opciones:
    1) Listado con todas las categorias incluidas
    2) Listado por categoria
    3) Menu anterior

      """)
      opcion_6= input("Teclee su respuesta y presione enter: ")
      if opcion_6=="1" and acceso==1:
        #lista top_resena_mayor[id producto, resena prom]
        print(""" 
              Lista de los 20 productos con la peor reseña
        """)
        #reverse para obtener las peores reseñas
        

        resena_menor= top_resena_mayor[:]
        resena_menor.reverse()
        resena_top_20= resena_menor[0:20]
        
        numeral=1
        
        
        while numeral<=20:
          for producto_bus in resena_top_20:
          
            for producto in lifestore_products:
              if producto_bus[0] == producto[0]:
                print(numeral, ".- ", producto[1], " calificación promedio: ", producto_bus[1])
                numeral += 1
                resena_top_20.remove(producto_bus)
                break
        #necesitamos añadir productos que no figuran en ventas, o mejor dicho que no se vendieron
        print("""
                        Productos sin reseña
                      
        """)
        numeral=1
        productos_no_bus= lifestore_products[:]

        
        for producto in resena_menor:
            
            for producto_bus in productos_no_bus:
              if producto_bus[0] == producto[0]:
                
                productos_no_bus.remove(producto_bus)
                break
        if len(productos_no_bus)>0:
          print("No tienen reseña un total de: ", len(productos_no_bus)," productos")
          print("A continuación se muestran algunos de ellos(20)")        
        
          for producto_no_buscado in productos_no_bus:
            if numeral<=20:  
              print(numeral, ".- ", producto_no_buscado[1], " Sin reseña")
              numeral += 1
        print("""
      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa
            """)
        cambio_op=input("Respuesta: ")
        if cambio_op == "a" :
          continue
        elif cambio_op == "b" :
          break
        else:
          no_op=0
          while no_op==0:
            print("Opción no valida, intente nuevamente")
            print("""

      ¿Que desea hacer?
      a) regresar al menu anterior
      b) salir del programa

            """)
            cambio_op=input("Respuesta: ")
            if cambio_op == "a" :
              no_op=1
              continue
            elif cambio_op == "b" :
              acceso=0
              no_op=1
              break
              



#inicia subopcion 2_________________________________
      if opcion_6=="2":
        while opcion_6=="2":
        #categorias productos
          print("""
              Productos con las peores reseñas

Si quiere ver el top 10 de productos con peores reseñas por categoria, seleccione una de las categorias a continuación
""")
          print("Total de categorias: ", len(categorias))
          numeral = 1
          for categoria in categorias:

            print(numeral, ".- ", categoria)
            numeral += 1
          intentos = 0
      
          busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
  """)
          valor="bien"
          try:
            busqueda = int(busqueda)
          except (ValueError):
            valor = "mal"

        
          if valor =="mal" and intentos<= 3:
            print("El valor ingresado no corresponde a alguna de las opciones")
            print("intente de nuevo")
            busqueda = input(
        """Teclee el numero de su selección y presione enter para continuar: 
            """)
            intentos += 1
            if intentos == 4:
              print("Intentos excedidos, reiniciando programa")
              acceso=0
            print("Intentos restantes: ", 4 - intentos)
     
          if acceso==1: 
            busqueda = int(busqueda)
            if busqueda == 0 or busqueda > len(categorias):
              print("""
    La opción que ha escogido es invalida.
      Verifique e intente nuevamente.
        """)

              intentos += 1
              #bucle deshabilitado
              if intentos == 4:
                print("Intentos excedidos, reiniciando programa")
                acceso=0
                break
              #print("Intentos restantes: ", 4 - intentos)
            
              continue
            else:
              busqueda = int(busqueda)
        
      

          if acceso==1:
            busqueda = categorias[busqueda-1]
#_______________________________________________-
#Comienza definición del top

        
            productos_copia = a

            lista_productos_req = []
            for producto in productos_copia:
              if producto[3] == busqueda:
                lista_productos_req.append(producto[0])
              else:
                continue
      #lista top_resena_mayor[id producto, resena prom]
        
            resena_menor= top_resena_mayor[:]
            resena_menor.reverse()
            resena_cat_top=resena_menor[:]
            numeral=1
            prod_cat_venta = []
            print("Lista con productos menos buscados de la categoria ", busqueda)
        
            for resena in resena_cat_top:
              if numeral<=20:
                for prod_cat in lista_productos_req:
                    if prod_cat == resena[0]:
                      for producto in lifestore_products:
                      
                        if resena[0]== producto[0]:
                    
                          print(numeral,".- ", producto[1], " calificación promedio: ", resena[1])
                          lista_productos_req.remove(prod_cat)
                          numeral+=1

                          break
          #necesario revisar articulos que no fueron vendidos
            numeral=1
            
            if len(lista_productos_req) > 0:
              print(""" 
                  Existen productos sin reseñas
                   Se enlistan a continuación
              """)
              print("Total de productos sin reseña: ", len(lista_productos_req), ", se enlistan solo 10")
              
              for prod_cat in lifestore_products:
                for producto in lista_productos_req:
                  if numeral<=10:
                    if producto== prod_cat[0]:
                      print(numeral, ".- ", prod_cat[1])
                      numeral+=1
                      lista_productos_req.remove(producto)
                      break
 
          print("""
      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) Salir del programa
            """)
          cambio_op=input("Respuesta: ")
          regresar_menu=0
          if cambio_op == "a" :
            opcion_6="2"
          elif cambio_op == "b" :
            break
          elif cambio_op == "c":
            acceso=0
            break
          else:
            no_op=0
            while no_op==0:
              print("Opción no valida, intente nuevamente")
              print("""

      ¿Que desea hacer?
      a) Seleccionar otra categoria
      b) Regresar al menu anterior
      c) salir del programa

            """)
              cambio_op=input("Respuesta: ")
              if cambio_op == "a" :
                no_op=1
                continue
              elif cambio_op=="b":
                no_op=1
                regresar_menu=1
                break
              elif cambio_op == "c" :
                acceso=0
                no_op=1
                break
          if regresar_menu== 1:
            break

      if opcion_6== "3":
        opcion=0
    


#opción 7 menú general
    while opcion=="7" and acceso==1:
      #ventas_mayor [indice producto, cantidad ventas]
      #lifestore_products[2] costo
      #lifestore_sales
      print("""
            Reporte de ventas
      """)
      acumulado=0
      # calcula el total con respecto a la lista de ventas
      for producto in lifestore_products:
        for venta in  copia_ventas_mayor:
          if venta[0]== producto[0]:
            venta_total= venta[1]*producto[2]
            acumulado=venta_total+acumulado
      print("Total de ventas: ", "$", acumulado)

      #sacar categorias
      fechas = []
      copia_lifestore_sales = lifestore_sales[:]

      fechas = []
      for fecha in copia_lifestore_sales:
        
        if fecha[3][3:] not in fechas:
            fechas.append(fecha[3][3:])
            
      #lista de fechas[fecha["mes/año"]]
      fechas.sort()

      #



      print("Meses con compras")
      print(""" 
      Si requiere calcular las ventas de un mes concreto, seleccione el mes que desee calcular
      """)
      numeral=1
      for fecha in fechas:
        print(numeral, ".- ",fecha,)
        numeral+=1
      
      #Seleccion regreso
      opt_7=0
      while opt_7==0:
        print("")
        print("Use solo numeros")
        busqueda=input("Selección: ")
      
        busqueda=int(busqueda)
        busqueda= fechas[busqueda-1]
      
        lista_cat_venta=[]
        for fecha in fechas:
          for venta in copia_lifestore_sales:
            if venta[3][3:] == busqueda and venta[4]==0:
              lista_cat_venta.append(venta[1])
              copia_lifestore_sales.remove(venta)
      #obtiene los valores de cada compra del mes
        print("")
        print("Total de ventas del mes: ", len(lista_cat_venta))
      #inicializar acumulado
        acumulado=0
        for elemento in lista_cat_venta:
          for producto in lifestore_products:
            if elemento==producto[0]:
            
              acumulado+= producto[2]

        print("La ganancia total del mes ", busqueda," es de $", acumulado)


      
  
      #menu de opciones
        print("""
      ¿Que desea hacer?
      a) Seleccionar otro mes
      b) Regresar al menu anterior
      c) Salir del programa
            """)
        cambio_op=input("Respuesta: ")
        if cambio_op=="a":
          continue
        elif cambio_op=="b":
          opcion=0
          break
        elif cambio_op=="c":
          opt_7=1
          break
        else:
          print("Opción invalida, vuelva a intentarlo")
          no_op=0
          while no_op==0:
            print("""
      ¿Que desea hacer?
      a) Seleccionar otro mes
      b) Regresar al menu anterior
      c) Salir del programa
            """)
        
            cambio_op=input("Respuesta: ")
            if cambio_op=="a":
              cambio_op==1
              continue
            elif cambio_op=="b":
              opcion=0
              no_op=1
            
            elif cambio_op=="b":
              no_op=1
            
            else:
              print("Opción invalida, vuelva a intentarlo")
              no_op=0
        if no_op==1 and cambio_op=="a":
          opción=0
          continue
        elif no_op==1 and cambio_op=="b":
          opt_7=1
          break
      if opt_7==1:
        break
  #
print("Finalizando programa")
#fin.... por fin...