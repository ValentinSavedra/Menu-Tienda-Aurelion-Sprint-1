# -*- coding: utf-8 -*-
"""
Script principal para el análisis de datos del Proyecto AURELION.
Este programa presenta un menú interactivo para acceder a diferentes
secciones del proyecto y mostrar las características de los datasets.

"""

# 1. IMPORTACIÓN DE LIBRERÍAS

import os

# 2. DEFINICIÓN DE FUNCIONES

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola. Es multiplataforma.
    """
    # 'os.name' nos dice el S.O. ('nt' para Windows, 'posix' para Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')



def mostrar_tema_problema_solucion():
    """
    Opción 2: Muestra la descripción del tema, problema y solución del proyecto.
    """
    limpiar_pantalla()
    print("===================================")
    print("== 2. Tema, problema y solución ==")
    print("===================================")
    
    print("""
    **Tema del Proyecto:**
    El dueño de la tienda Aurelion solicita el servicio de la corporación
    Chronos Data (Datos del tiempo). Para este trabajo fuimos seleccionados
    nosotros, el conjunto 7, analistas especializados en base de datos.

    **Problema a Resolver:**
    A partir de este estudio se determinó que la tienda cuenta con datos
    valiosos pero desorganizados, lo que limita darle respuesta a las
    siguientes problemáticas e interrogantes para que se pueda tener
    una dinámica provechosa en la tienda:

    1. Ignorancia del cliente ideal:
       No se identifican los clientes con valor (Por su frecuencia o
       cantidad de compras).
       - ¿Quiénes son nuestros clientes más valiosos y cómo podemos
         segmentarlos para desarrollar un programa de fidelización
         efectivo?

    2. Gestión del inventario ineficaz:
       A causa de una mala identificación de productos más y menos
       solicitados se genera un exceso de stock.
       - ¿Cuáles son los productos con la mayor y menor rotación para
         optimizar los niveles de stock, reducir el inventario
         estancado y asegurar la disponibilidad de los artículos
         más solicitados?

    3. Análisis de venta ineficiente:
       Conseguir métricas básicas (como ventas por categoría, ciudad o
       método de pago) conlleva un proceso manual, lento y propenso a
       errores, reduciendo la capacidad de tomar decisiones rápidas.
       - ¿Cómo podemos automatizar los reportes de ventas y tendencias
         desglosadas por categoría, ciudad y método de pago, para
         tener información eficiente?

    4. Despiste de posibles oportunidades comerciales:
       Al no identificar patrones de compras como productos que se
       compran juntos, para planificar promociones y la disposición
       de productos en la tienda.
       - ¿Qué combinaciones de productos se compran juntos con mayor
         frecuencia, para poder crear promociones y optimizar la
         disposición de los productos en la tienda?

    **Solución Propuesta:**

    SOLUCIÓN DE CIENTÍFICOS DE BASES DE DATOS
    Creación de un sistema interactivo de consulta y análisis para la tienda.
    
    1. Motor de procesamiento con Python:
       - Unificación de Datos: El programa cargará y unificará las tablas
         en un único dataset coherente, aplicando el concepto de claves
         primarias y foráneas.
       - Análisis automatizado: Integrar funciones específicas que
         responderán más preguntas claves del negocio, empleando
         estructuras de control y colecciones.
         Ej: calcular_top_clientes(), identificar_productos_más_solicitados()
       - Interfaz de Consulta Interactiva: Programa con un menú que
         permite seleccionar qué información se desea ver.
         Ej: Presione 1 para ver el top 5 de clientes.
         Haciendo los datos accesibles sin necesidad de conocimientos técnicos.
    
    2. Dashboard Visual en Power BI:
       - Los resultados más importantes generados por Python se
         conectarán a un Dashboard en Power BI.
       - Dicho tablero enseñará de forma visual y clara:
         -- Métricas principales (Total de Ventas, clientes únicos).
         -- Gráfico de los productos más vendidos y categorías.
         -- Un mapa o gráfico de las ventas por ciudad.
         -- Esto da paso a la solución de "no poder ingresar a los
            insights" de un vistazo.
    
    3. Documentación Exhaustiva (Documentación.md):
       - Problema y Solución: Establecerá detalladamente el problema
         y como está solución lo solventa.
       - Fuente y Estructura de Datos: Describe la base de datos
         (las 4 tablas), sus campos, tipos de datos y relacionales.
       - Pseudocódigo y Diagrama de Flujo: Se integrará por el desglose
         del algoritmo principal y su diagrama.
       - Instrucciones para Copilot: Expondrá los prompts utilizados
         para generar partes del código, exponiendo el trabajo
         aunado a la IA.

    ----------------------------------------------------------------------

    SOLUCIONES EXPUESTAS AL DUEÑO DE LA TIENDA
    Para transformar la información de la tienda en decisiones inteligentes
    que aumenten el ingreso desarrollaremos "El Tablero de Control Aurelion",
    un sistema fácil de usar que le dará respuestas claras:

    RESPUESTAS A LAS INTERROGANTES:
    1. ¿Quiénes son sus clientes más valiosos?
       - Respuesta: Al escribir un simple comando, el sistema le mostrará
         una lista con sus "Top 5 clientes estrella".
       - Beneficio: Se propicia el envío de ofertas especiales o
         agradecimientos personales, para asegurar la compra continua.

    2. ¿Qué productos se venden más y cuáles menos?
       - Respuesta: El sistema presentará dos listas claras:
         "Productos campeones" y "Productos Lentos".
       - Beneficio: No se acabará el stock de aquellos productos más
         vendidos y se da la oportunidad de desarrollar promociones.

    3. ¿Cómo ver rápidamente las ventas por categoría, ciudad o método de pago?
       - Respuesta: En una pantalla con gráficos coloridos y fáciles de
         entender, se podrá ver qué categoría vende más, en qué ciudad
         se tienen más tiendas y métodos de pago preferidos.
       - Beneficio: Agilizará la toma de decisiones mediante una
         consciencia de lo más beneficioso para el negocio.

    4. ¿Qué productos se compran juntos?
       - Respuesta: El sistema revelará "Pareja de productos" que los
         clientes tienden a comprar en conjunto.
       - Beneficio: Se podrán crear ofertas combinadas propiciando el
         aumento de compras.

    UTILIDAD A LARGO PLAZO
    - Análisis rápidos: El dueño o el equipo mediante la ejecución del
      programa podrán elegir alguna opción del menú para conocer el
      aspecto requerido según la preferencia.
    - Para reuniones y planificación: El acceso a un "Tablero visual"
      con gráficos profesionales que se pueden visualizar en computadoras
      o teléfonos, facilitará la toma de decisiones.
    """)
    print("=" * 35)
    input("\nPresiona Enter para volver al menú...")

def mostrar_informacion_equipo():
    """
    Opción 1: Muestra información sobre los integrantes del equipo.
    """
    limpiar_pantalla()
    print("===========================")
    print("== 1. Información del equipo ==")
    print("===========================")
    
    print("""
    * Integrante 1: Valentín Savedra
    * Rol: Científico de Datos
    * Contacto: 7valennico2010@gmail.com

    * Integrante 2: Marcos Amadori
    * Rol: Científico de Datos
    * Contacto: viasapiens1701@gmail.com

    * Integrante 3: Andrés Segura
    * Rol: Científico de Datos
    * Contacto: andrealex2407@gmail.com
          
    * Integrante 4: Melina Selaye
    * Rol: Científico de Datos
    * Contacto: melinaselayeunlz@gmail.com
          
    * Integrante 5: Gabriela Hernández
    * Rol: Científico de Datos
    * Contacto: gabrielahm.1308@gmail.com
    
    * Integrante 6: Johan Meza
    * Rol: Científico de Datos
    * Contacto: johanmezasalazar@gmail.com
          
    * Integrante 7: Luis Cristóbal Zegarra
    * Rol: Científico de Datos
    * Contacto: cristze196@gmail.com
    
    * Integrante 8: Germán Stengel
    * Rol: Científico de Datos
    * Contacto: german.stengel09@gmail.com
    
    * Integrante 9: Antonella Bustamante
    * Rol: Científico de Datos
    * Contacto: antobustamante14.1@gmail.com
    """)
          
    print("=" * 27) 
    input("\nPresiona Enter para volver al menú...")

def mostrar_datasets():
    """
    Opción 3: Muestra las tablas de características (diccionario de datos)
    de las 4 tablas base: Ventas, Productos, Detalle_Ventas y Clientes.
    """
    limpiar_pantalla()
    print("===========================================================================")
    print("== 3. Dataset: Características de las 4 Tablas Base ==")
    print("===========================================================================")
    
    
    c1_ancho = 17 # Ancho de "Escalas de medida"
    c2_ancho = 65 # Ancho ajustado para el contenido
    
    # Creamos las líneas de la tabla
    linea_superior = "+" + "-"*(c1_ancho + 2) + "+" + "-"*(c2_ancho + 2) + "+"
    linea_header   = "+" + "="*(c1_ancho + 2) + "+" + "="*(c2_ancho + 2) + "+"
    
    
    # --- INICIO TABLA VENTAS ---
    
    print("\nTABLA: Características de [VENTAS]")
    
    print(linea_superior)
    print(f"| {'CARACTERÍSTICA':<{c1_ancho}} | {'DESCRIPCIÓN':<{c2_ancho}} |")
    print(linea_header)
    print(f"| {'Origen':<{c1_ancho}} | {'Primario':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Definición':<{c1_ancho}} | {'Registro de transacciones de ventas realizadas en la tienda':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Estructura':<{c1_ancho}} | {'Estructurado':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Tipos de datos':<{c1_ancho}} | {'Cuantitativos: id_venta, id_cliente':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'Cualitativos: fecha, nombre_cliente, email, medio_pago':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Escalas de medida':<{c1_ancho}} | {'Nominal: medio_pago, nombre_cliente, email':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'Ordinal: | Intervalo: fecha | Razón: id_venta, id_cliente':<{c2_ancho}} |")
    print(linea_superior)
    
    # --- FIN TABLA VENTAS ---
    
    
    print("\n\n") # Separador entre tablas
    
    
    # --- INICIO TABLA PRODUCTOS ---
    
    print("TABLA: Características de [PRODUCTOS]")
    
    print(linea_superior)
    print(f"| {'CARACTERÍSTICA':<{c1_ancho}} | {'DESCRIPCIÓN':<{c2_ancho}} |")
    print(linea_header)
    print(f"| {'Origen':<{c1_ancho}} | {'Primario':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Definición':<{c1_ancho}} | {'Inventario de productos a la venta':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Estructura':<{c1_ancho}} | {'Estructurada':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Tipos de datos':<{c1_ancho}} | {'Cuantitativos: id_producto, precio_unitario':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'Cualitativos: nombre_producto, categoría':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Escalas de medida':<{c1_ancho}} | {'Nominal: nombre_producto, categoría | Ordinal: | Intervalo:':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'| Razón: id_producto, precio_unitario':<{c2_ancho}} |")
    print(linea_superior)
    
    # --- FIN TABLA PRODUCTOS ---

    
    print("\n\n") # Separador entre tablas

    
    # --- INICIO TABLA DETALLE_VENTAS ---
    
    print("TABLA: Características de [DETALLE_VENTAS]")
    
    print(linea_superior)
    print(f"| {'CARACTERÍSTICA':<{c1_ancho}} | {'DESCRIPCIÓN':<{c2_ancho}} |")
    print(linea_header)
    print(f"| {'Origen':<{c1_ancho}} | {'Primario':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Definición':<{c1_ancho}} | {'Productos vendidos en cada transacción':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Estructura':<{c1_ancho}} | {'Estructurado':<{c2_ancho}} |")
    print(linea_superior)
    
    # (Ajuste de 3 líneas para que quepa bien)
    print(f"| {'Tipos de datos':<{c1_ancho}} | {'Cuantitativos: id_venta, id_producto, cantidad,':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'precio_unitario, importe':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'| Cualitativos: nombre_producto':<{c2_ancho}} |")
    print(linea_superior)
    
    print(f"| {'Escalas de medida':<{c1_ancho}} | {'Nominal: nombre_cliente, email, ciudad | Ordinal:':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'| Intervalo: fecha_alta | Razón: id_cliente':<{c2_ancho}} |")
    print(linea_superior)
    
    # --- FIN TABLA DETALLE_VENTAS ---

    
    print("\n\n") # Separador entre tablas

    
    # --- INICIO TABLA CLIENTES ---
    
    print("TABLA: Características de [CLIENTES]")
    
    print(linea_superior)
    print(f"| {'CARACTERÍSTICA':<{c1_ancho}} | {'DESCRIPCIÓN':<{c2_ancho}} |")
    print(linea_header)
    print(f"| {'Origen':<{c1_ancho}} | {'Primario':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Definición':<{c1_ancho}} | {'Información demográfica y de registro de clientes':<{c2_ancho}} |")
    print(linea_superior)
    print(f"| {'Estructura':<{c1_ancho}} | {'Estructurado':<{c2_ancho}} |")
    print(linea_superior)
    
    print(f"| {'Tipos de datos':<{c1_ancho}} | {'Cuantitativos: id_clientes':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'Cualitativos: nombre_cliente, email, ciudad, fecha_alta':<{c2_ancho}} |")
    print(linea_superior)
    
    print(f"| {'Escalas de medida':<{c1_ancho}} | {'Nominal: nombre_cliente, email, ciudad | Ordinal:':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'| Intervalo: fecha_alta | Razón: id_cliente':<{c2_ancho}} |")
    print(linea_superior)
    
    # --- FIN TABLA CLIENTES ---
    
    
    print("\n")
    print("=" * 73) # Ajustamos al ancho del nuevo título
    input("\nPresiona Enter para volver al menú...")


def mostrar_info_pasos_estructura():
    """
    Opción 4: Muestra información sobre pasos, pseudocódigo y diagrama.
    """
    limpiar_pantalla()
    print("=====================================================")
    print("== 4. Información, pasos, pseudocódigo y diagrama ==")
    print("=====================================================")
    
    print("""
    ** INFORMACIÓN **

    **Tema del Proyecto:**
    TIENDA AURELION
    DATOS VALIOSOS PERO DESORGANIZADOS

    El dueño de la tienda Aurelion solicita el servicio de la corporación Chronos
    Data (Datos del tiempo). Para este trabajo fuimos seleccionados nosotros,
    el conjunto 7, analistas especializados en base de datos. Para poder dar
    inicio a nuestro trabajo nos encargamos de examinar minuciosamente la
    base de datos otorgada por el dueño de la tienda. A partir de este estudio
    se determinó que la tienda cuenta con datos valiosos pero desorganizados,
    lo que limita darle respuesta a las siguientes problemáticas e interrogantes
    para que se pueda tener una dinámica provechosa en la tienda.

    ----------------------------------------------------------------------

    **Problema a Resolver:**

    1. Ignorancia del cliente ideal:
       No se identifican los clientes con valor (Por su frecuencia o
       cantidad de compras).
       - ¿Quiénes son nuestros clientes más valiosos y cómo podemos
         segmentarlos para desarrollar un programa de fidelización
         efectivo?

    2. Gestión del inventario ineficaz:
       A causa de una mala identificación de productos más y menos
       solicitados se genera un exceso de stock.
       - ¿Cuáles son los productos con la mayor y menor rotación para
         optimizar los niveles de stock, reducir el inventario
         estancado y asegurar la disponibilidad de los artículos
         más solicitados?

    3. Análisis de venta ineficiente:
       Conseguir métricas básicas (como ventas por categoría, ciudad o
       método de pago) conlleva un proceso manual, lento y propenso a
       errores, reduciendo la capacidad de tomar decisiones rápidas.
       - ¿Cómo podemos automatizar los reportes de ventas y tendencias
         desglosadas por categoría, ciudad y método de pago, para
         tener información eficiente?

    4. Despiste de posibles oportunidades comerciales:
       Al no identificar patrones de compras como productos que se
       compran juntos, para planificar promociones y la disposición
       de productos en la tienda.
       - ¿Qué combinaciones de productos se compran juntos con mayor
         frecuencia, para poder crear promociones y optimizar la
         disposición de los productos en la tienda?

    ----------------------------------------------------------------------

    **Solución Propuesta:**

    SOLUCIÓN DE ANALISTAS DE BASE DE DATOS
    Creación de un sistema interactivo de consulta y análisis para la tienda.
    
    1. Motor de procesamiento con Python:
       - Unificación de Datos: El programa cargará y unificará las tablas
         en un único dataset coherente, aplicando el concepto de claves
         primarias y foráneas.
       - Análisis automatizado: Integrar funciones específicas que
         responderán más preguntas claves del negocio.
         (Ej: calcular_top_clientes(), analizar_ventas_por_ciudad()).
       - Interfaz de Consulta Interactiva: Programa con un menú que
         permite seleccionar qué información se desea ver.
         (Ej: Presione 1 para ver el top 5 de clientes).

    2. Dashboard Visual en Power BI:
       - Los resultados más importantes generados por Python se
         conectarán a un Dashboard en Power BI.
       - Dicho tablero enseñará de forma visual y clara:
         -- Métricas principales (Total de Ventas, clientes únicos).
         -- Gráfico de los productos más vendidos y categorías.
         -- Un mapa o gráfico de las ventas por ciudad.

    3. Documentación Exhaustiva (Documentación.md):
       - Problema y Solución: Detallará el problema y cómo la
         solución lo solventa.
       - Fuente y Estructura de Datos: Describe la base de datos
         (las 4 tablas), sus campos, tipos de datos y relacionales.
       - Pseudocódigo y Diagrama de Flujo: Desglose del algoritmo
         principal y su diagrama.
       - Instrucciones para Copilot: Expondrá los prompts utilizados
         para generar partes del código.

    SOLUCIONES EXPUESTAS AL DUEÑO DE LA TIENDA
    Para transformar la información de la tienda en decisiones inteligentes
    desarrollaremos "El Tablero de Control Aurelion", un sistema fácil de
    usar que le dará respuestas claras:

    Respuestas a las interrogantes:
    1. ¿Quiénes son sus clientes más valiosos?
       - Respuesta: El sistema le mostrará una lista "Top 5 clientes estrella".
       - Beneficio: Propicia el envío de ofertas especiales o
         agradecimientos personales.

    2. ¿Qué productos se venden más y cuáles menos?
       - Respuesta: El sistema presentará "Productos campeones" y
         "Productos Lentos".
       - Beneficio: Evita roturas de stock y permite liquidar
         inventario lento.

    3. ¿Cómo ver rápidamente las ventas?
       - Respuesta: Gráficos coloridos mostrarán ventas por categoría,
         ciudad y método de pago.
       - Beneficio: Agiliza la toma de decisiones.

    4. ¿Qué productos se compran juntos?
       - Respuesta: El sistema revelará "Pareja de productos".
       - Beneficio: Se podrán crear ofertas combinadas.
    """)
    

    print("\n" + "="*70 + "\n")
  
    print("""
    PASOS DEL PROYECTO:
    1.  **Definición del Problema:** Entender la necesidad del negocio.
    2.  **Recolección de Datos:** Obtener los datasets iniciales (los 4 CSVs).
    3.  **Limpieza y Preprocesamiento:** Unificar tablas, manejar valores nulos, etc.
    4.  **Análisis Exploratorio de Datos:** Calcular estadísticas, 
        responder preguntas (ej. ¿Producto más vendido? ¿Cliente que más compra?).
    5.  **Visualización:** Crear gráficos para comunicar los hallazgos.
    6.  **Conclusiones:** Generar insights y recomendaciones para el negocio.
    
    PSEUDOCÓDIGO DEL MENÚ:
    INICIO
        BUCLE infinito
            LIMPIAR pantalla
            MOSTRAR menú de opciones (1-6)
            PEDIR al usuario que elija una opción
            
            SI opción = 1, LLAMAR función 'mostrar_informacion_equipo'
            SI opción = 2, LLAMAR función 'mostrar_tema_problema_solucion'
            SI opción = 3, LLAMAR función 'mostrar_datasets'
            SI opción = 4, LLAMAR función 'mostrar_info_pasos_estructura'
            SI opción = 5, LLAMAR función 'mostrar_sugerencias'
            SI opción = 6,
                MOSTRAR mensaje de despedida
                ROMPER bucle
            SINO (opción no es 1-6),
                MOSTRAR mensaje de error
            
            ESPERAR que el usuario presione Enter (excepto al salir)
        FIN BUCLE
    FIN
    
          
    DIAGRAMA DE FLUJO:
    
    [Inicio] -> [Cargar Datos] -> [Unificar Datos] -> [Mostrar Menú] -> [Leer Opción]
                          ^                                   |
                          |                                   v
                           < - [Ejecutar Análisis] < - [Validar Opción]
                                               |
                                               v
                                 [Exportar Resultados] -> [Power BI] -> [Fin]
    
    """)
    print("=" * 53)
    input("\nPresiona Enter para volver al menú...")

def mostrar_sugerencias():
    """
    Opción 5: Muestra las sugerencias de la IA (no implementadas).
    """
    limpiar_pantalla()
 
    print("=========================================")
    print("== 5. Sugerencias de la IA ==")
    print("=========================================")


    print("""
Sugerencias de la IA (no implementadas):

 1. Robustez en la Entrada del Menú (Validación de Usuario)
Problema Identificado: El script actualmente lee la entrada del menú (opcion = input(...))
como una cadena de texto. Si el usuario ingresa un valor no numérico (ej. "hola")
o un número fuera de rango, la estructura if-elif-else simplemente no encuentra
una coincidencia y vuelve a mostrar el menú, sin informar al usuario del error.

Solución Recomendada: Implementar un bloque try-except para validar la entrada.
El objetivo es intentar convertir la entrada a un entero y capturar la
excepción ValueError si falla.

Ejemplo de Implementación:
Python
opcion_str = input("Elija una opción: ")
try:
    opcion = int(opcion_str)
    if opcion == 1:
        # ...
    elif opcion == 6: 
        break
    else:
        # Manejar números fuera de rango (ej. 7, 8)
        print("\\nOpción no válida. Por favor, ingrese un número del 1 al 6.")
        input("Presiona Enter para continuar...")

except ValueError:
    # Manejar entradas no numéricas (ej. "a", "hola")
    print(f"\\nError: '{opcion_str}' no es una entrada válida. Debe ingresar un número.")
    input("Presiona Enter para continuar...")


 2. Optimización de Carga de Datos (Caching del Dataset)
Problema Identificado: La Opción 3 (cargar_y_unificar_dataset) lee los cuatro
archivos CSV, los carga en memoria y realiza el costoso proceso de merge cada
vez que el usuario selecciona la opción. Si los datasets crecen, esto generará
una demora notable e innecesaria en cada consulta.

Solución Recomendada: Implementar un sistema de "caching". La primera vez que
los datos se unifiquen, el DataFrame resultante debe guardarse en un formato de
archivo rápido y optimizado (como Parquet o Feather). En las siguientes ejecuciones,
la función primero debe verificar si este archivo cache existe.
    Si existe: Carga el archivo Parquet (mucho más rápido que leer y unir 4 CSVs).
    Si no existe: Realiza el proceso de merge completo y crea el archivo Parquet.


 3. Modularización del Código (Separación de Lógica)
Problema Identificado: Actualmente, todo el código reside en un único script.
La lógica de la interfaz de usuario (el menú main()) está mezclada con la lógica
de procesamiento de datos (la función cargar_y_unificar_dataset()).

Solución Recomendada: Separar el código en (al menos) dos archivos distintos:
    menu_proyecto.py: Contendría toda la lógica del menú (main(), prints, etc.).
    procesador_datos.py: Contendría la lógica de datos (cargar_y_unificar_dataset())
                          y la importación de pandas.
El archivo menu_proyecto.py importaría la función que necesita desde el otro
archivo (ej: from procesador_datos import cargar_y_unificar_dataset).
""")
    print("=" * 41)
    input("\nPresiona Enter para volver al menú...")


# 3. LÓGICA PRINCIPAL

def main():
    """
    Función principal que ejecuta el menú interactivo.
    """
    while True:
        limpiar_pantalla()
        
        print("""
        == Menú de secciones ==
        1. Información del equipo
        2. Tema, problema y solución
        3. Dataset de referencia
        4. Información, pasos, pseudocódigo y diagrama
        5. Sugerencias y mejoras de Copilot
        6. Salir
        """)
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            mostrar_informacion_equipo()
        elif opcion == '2':
            mostrar_tema_problema_solucion()
        elif opcion == '3':
            mostrar_datasets()
        elif opcion == '4':
            mostrar_info_pasos_estructura()
        elif opcion == '5':
            mostrar_sugerencias()
        elif opcion == '6':
            print("\nFIN\nGracias por utilizar el programa. ¡Hasta pronto!")
            break
        else:
            print(f"\nOpción '{opcion}' no válida. Por favor, ingrese un número del 1 al 6.")
            input("Presiona Enter para continuar...")

# 4. PUNTO DE ENTRADA

if __name__ == "__main__":
    main()
