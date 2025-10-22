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
 
    os.system('cls' if os.name == 'nt' else 'clear')

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
    """)
          
    print("=" * 27) 
    input("\nPresiona Enter para volver al menú...")

def mostrar_tema_problema_solucion():
    """
    Opción 2: Muestra la descripción del tema, problema y solución del proyecto.
    """
    limpiar_pantalla()
    print("===================================")
    print("== 2. Tema, problema y solución ==")
    print("===================================")
    
    # --- ¡EDITAR ESTE TEXTO! ---
    print("""
    **Tema del Proyecto:**
    [Describe aquí el tema central de tu proyecto.]

    **Problema a Resolver:**
    [Detalla aquí el problema específico que buscas abordar.]

    **Solución Propuesta:**
    [Explica cómo tu proyecto o análisis ayudará a resolver el problema.]
    """)
    print("=" * 35)
    input("\nPresiona Enter para volver al menú...")

def cargar_y_unificar_dataset():
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
    
    
    # INICIO TABLA VENTAS
    
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
    
    # FIN TABLA VENTAS
    
    
    print("\n\n") # Separador entre tablas
    
    
    
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
    

    
    print("\n\n") # Separador entre tablas

    
    
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
    
    print(f"| {'Tipos de datos':<{c1_ancho}} | {'Cuantitativos: id_venta, id_producto, cantidad,':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'precio_unitario, importe':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'| Cualitativos: nombre_producto':<{c2_ancho}} |")
    print(linea_superior)
    
    print(f"| {'Escalas de medida':<{c1_ancho}} | {'Nominal: nombre_cliente, email, ciudad | Ordinal:':<{c2_ancho}} |")
    print(f"| {'':<{c1_ancho}} | {'| Intervalo: fecha_alta | Razón: id_cliente':<{c2_ancho}} |")
    print(linea_superior)
    

    
    print("\n\n") # Separador entre tablas

    
    
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
    
    
    
    print("\n")
    print("=" * 73) 
    input("\nPresiona Enter para volver al menú...")


def mostrar_info_pasos_estructura():
    """
    Opción 4: Muestra información sobre pasos, pseudocódigo y diagrama.
    """
    limpiar_pantalla()
    print("=====================================================")
    print("== 4. Información, pasos, pseudocódigo y diagrama ==")
    print("=====================================================")
    
    # ¡EDITAR ESTE TEXTO!
    print("""
    **Pasos del Proyecto:**
    1.  **Definición del Problema:** Entender la necesidad del negocio.
    2.  **Recolección de Datos:** Obtener los datasets iniciales (los 4 CSVs).
    3.  **Limpieza y Preprocesamiento:** Unificar tablas, manejar valores nulos, etc.
    4.  **Análisis Exploratorio de Datos (EDA):** Calcular estadísticas, 
        responder preguntas (ej. ¿Producto más vendido? ¿Cliente que más compra?).
    5.  **Visualización:** Crear gráficos para comunicar los hallazgos.
    6.  **Conclusiones:** Generar insights y recomendaciones para el negocio.
    
    **Pseudocódigo del Menú:**
    INICIO
        BUCLE infinito
            LIMPIAR pantalla
            MOSTRAR menú de opciones (1-6)
            PEDIR al usuario que elija una opción
            
            SI opción es 1, LLAMAR función 'mostrar_informacion_equipo'
            SI opción es 2, LLAMAR función 'mostrar_tema_problema_solucion'
            SI opción es 3, LLAMAR función 'cargar_y_unificar_dataset'
            SI opción es 4, LLAMAR función 'mostrar_info_pasos_estructura'
            SI opción es 5, LLAMAR función 'mostrar_sugerencias'
            SI opción es 6,
                MOSTRAR mensaje de despedida
                ROMPER bucle
            SINO (opción no es 1-6),
                MOSTRAR mensaje de error
            
            ESPERAR que el usuario presione Enter (excepto al salir)
        FIN BUCLE
    FIN
    
    **Diagrama de Flujo:**
    [Descripción textual del diagrama de flujo]
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
            cargar_y_unificar_dataset()
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
