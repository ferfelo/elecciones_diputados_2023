import csv
import random

archivo = 'candidatos2023.csv'

escanios_por_distrito = {
    'BUENOS AIRES': 35,
    'CATAMARCA': 2,
    'CHACO': 3,
    'CHUBUT': 3,
    'CIUDAD AUTONOMA DE BUENOS AIRES': 12,
    'CORDOBA': 10,
    'CORRIENTES': 4,
    'ENTRE RIOS': 4,
    'FORMOSA': 3,
    'JUJUY': 3,
    'LA PAMPA': 2,
    'LA RIOJA': 2,
    'MENDOZA': 5,
    'MISIONES': 3,
    'NEUQUEN': 3,
    'RIO NEGRO': 3,
    'SALTA': 4,
    'SAN JUAN': 3,
    'SAN LUIS': 2,
    'SANTA CRUZ': 2,
    'SANTA FE': 10,
    'SANTIAGO DEL ESTERO': 4,
    'TIERRA DEL FUEGO': 3,
    'TUCUMAN': 5
}

electores_por_distrito = {
    'BUENOS AIRES': 13110768,
    'CATAMARCA': 340168,
    'CHACO': 1001813,
    'CHUBUT': 474242,
    'CIUDAD AUTONOMA DE BUENOS AIRES': 2533092,
    'CORRIENTES': 933876,
    'CORDOBA': 3065088,
    'ENTRE RIOS': 1143459,
    'FORMOSA': 482602,
    'JUJUY': 590861,
    'LA PAMPA': 300160,
    'LA RIOJA': 304456,
    'MENDOZA': 1492379,
    'MISIONES': 988482,
    'NEUQUEN': 553748,
    'RIO NEGRO': 595081,
    'SALTA': 1090057,
    'SAN JUAN': 608535,
    'SAN LUIS': 421370,
    'SANTA CRUZ': 265330,
    'SANTA FE': 2818280,
    'SANTIAGO DEL ESTERO': 812080,
    'TIERRA DEL FUEGO': 148020,
    'TUCUMAN': 1320478
}

resultados_votos = [
    "BUENOS AIRES",
    {"FRENTE DE IZQUIERDA Y DE TRABAJADORES": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00
     },
    "CATAMARCA",
    {"JUNTOS POR EL CAMBIO": 00,
     "LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00
     },
    "CHACO",
    {"JUNTOS POR EL CAMBIO": 00,
     "LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00
     },
    "CHUBUT",
    {"FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD": 00,
     "JUNTOS POR EL CAMBIO CHUBUT": 00,
     "LA LIBERTAD AVANZA CHUBUT": 00,
     "UNION POR LA PATRIA": 00
     },
    "CIUDAD AUTONOMA DE BUENOS AIRES",
    {"FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00
     },
    "CORDOBA",
    {"FRENTE DE IZQUIERDA Y DE LOS TRABAJADORES-UNIDAD": 00,
     "HACEMOS POR NUESTRO PAIS": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00
     },
    "CORRIENTES",
    {"ENCUENTRO POR CORRIENTES - ECO + VAMOS CORRIENTES": 00,
     "LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00
     },
    "ENTRE RIOS",
    {"JUNTOS POR ENTRE RIOS": 00,
     "MAS PARA ENTRE RIOS": 00,
     "LA LIBERTAD AVANZA": 00
     },
    "FORMOSA",
    {"LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00,
     "JUNTOS POR EL CAMBIO": 00
     },
    "JUJUY",
    {"FRENTE DE IZQUIERDA Y DE TRABAJADORES-UNIDAD": 00,
     "CAMBIA JUJUY": 00,
     "PARTIDO RENOVADOR FEDERAL": 00,
     "UNION POR LA PATRIA": 00
     },
    "LA PAMPA",
    {"FRENTE DE IZQUIERDA Y DE TRABAJADORES": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "UNION POR LA PATRIA": 00
     },
    "LA RIOJA",
    {"DEMOCRATA CRISTIANO": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00
     },
    "MENDOZA",
    {"CAMBIA MENDOZA": 00,
     "FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD": 00,
     "MOVIMIENTO LIBRES DEL SUR": 00,
     "LA LIBERTAD AVANZA": 00,
     "UNION POR LA PATRIA": 00
     },
    "MISIONES",
    {"FRENTE RENOVADOR DE LA CONCORDIA-INNOVACION FEDERAL MNES": 00,
     "JUNTOS POR EL CAMBIO MNES": 00,
     "PARTIDO AGRARIO Y SOCIAL MNES": 00
     },
    "NEUQUEN",
    {"FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD": 00,
     "ARRIBA NEUQUEN": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "MOVIMIENTO POPULAR NEUQUINO": 00,
     "UNION POR LA PATRIA": 00
     },
    "RIO NEGRO",
    {"FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "JUNTOS SOMOS RIO NEGRO": 00,
     "PARTIDO FE": 00,
     "UNION POR LA PATRIA": 00
     },
    "SALTA",
    {"AHORA PATRIA": 00,
     "FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "PARTIDO AUTONOMISTA": 00,
     "SI-SALTA INDEPENDIENTE": 00,
     "UNION POR LA PATRIA": 00
     },
    "SAN JUAN",
    {"ALIANZA JUNTOS POR EL CAMBIO": 00,
     "FRENTE UNION POR LA PATRIA - SAN JUAN": 00,
     "LA LIBERTAD AVANZA": 00
     },
    "SAN LUIS",
    {"ALIANZA FRENTE DE IZQUIERDA Y DE TRABAJADORES UNIDAD  SAN LUIS": 00,
     "ALIANZA LA LIBERTAD AVANZA SAN LUIS": 00,
     "JUNTOS POR EL CAMBIO  SAN LUIS": 00,
     "PARTIDO UNION Y LIBERTAD SAN LUIS": 00,
     "PARTIDO POR SAN LUIS": 00},
    "SANTA CRUZ",
    {"ALIANZA CAMBIA SANTA CRUZ": 00,
     "ALIANZA FRENTE DE IZQUIERDA Y DE LOS TRABAJADORES-UNIDAD": 00,
     "ALIANZA POR SANTA CRUZ": 00,
     "ALIANZA UNION POR LA PATRIA": 00
     },
    "SANTA FE",
    {"ALIANZA FRENTE DE IZQUIERDA Y TRABAJADORES- UNIDAD": 00,
     "ALIANZA JUNTOS POR EL CAMBIO": 00,
     "ALIANZA LA FUERZA DE SANTA FE": 00,
     "ALIANZA LA LIBERTAD AVANZA": 00,
     "ALIANZA UNION POR LA PATRIA": 00
     },
    "SANTIAGO DEL ESTERO",
    {"FRENTE CIVICO POR SANTIAGO": 00,
     "FRENTE RENOVADOR": 00,
     "JUNTOS POR EL CAMBIO": 00
     },
    "TIERRA DEL FUEGO",
    {"ALIANZA FRENTE DE IZQUIERDA DE TRABAJADORES - UNIDAD": 00,
     "ALIANZA HACEMOS POR NUESTRO PAIS": 00,
     "ALIANZA JUNTOS POR EL CAMBIO TDF": 00,
     "ALIANZA UNION POR LA PATRIA": 00,
     "REPUBLICANOS UNIDOS": 00,
     "SOMOS FUEGUINOS": 00
     },
    "TUCUMAN",
    {"FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD": 00,
     "FRENTE UNION POR LA PATRIA": 00,
     "FUERZA REPUBLICANA": 00,
     "JUNTOS POR EL CAMBIO": 00,
     "MOVIMIENTO LIBRES DEL SUR": 00
     }
]


def sumar_votos_por_distrito(resultados):
    votos_por_distrito = {}  # Diccionario para almacenar los votos por distrito

    # Iterar a través de la lista de resultados_votos
    for i in range(0, len(resultados), 2):
        distrito = resultados[i]  # Nombre del distrito
        votos = resultados[i + 1]  # Votos por partido en ese distrito

        # Sumar los votos de cada partido en el distrito
        total_votos_distrito = sum(votos.values())

        # Almacenar el total de votos en el diccionario
        votos_por_distrito[distrito] = total_votos_distrito

    return votos_por_distrito


def comparacion_votos_electores(votos_por_distrito, electores):
    print("***************Cantidad de votos - Cantidad de electores por distrito ***************")

    for distrito in votos_por_distrito.keys():
        votos1 = votos_por_distrito[distrito]
        votos2 = electores[distrito]
        print(f'{distrito}: {votos1} votos - {votos2} electores')
        # Verifica si los votos son mas que los electores (error en la carga de datos o fraude)
        if votos1 > votos2:
            print(f'Los votos en {distrito} son mayores que los electores')


def leer_archivo_csv(file_name):
    lista_candidatos = []
    with open(file_name, 'r', encoding='ISO-8859-1') as csvfile:
        lector_csv = csv.reader(csvfile, delimiter=',')

        for fila in lector_csv:
            if fila[4] == "TITULARES":
                distrito = fila[0]
                partido = fila[1]
                posicion = int(fila[5])  # Convertir la posición a un entero
                nombre = fila[6]
                lista_candidatos.append((distrito, partido, posicion, nombre))

    return lista_candidatos


def obtener_candidatos_ganadores(lista_candidatos, escanios):
    candidatos_ganadores = []
    contador = 1
    print("*********************** CANDIDATOS ELECTOS ***********************")
    for distrito_escanio, partido_escanio, escanio in escanios:
        for distrito, partido, posicion, nombre in lista_candidatos:
            if distrito == distrito_escanio and partido == partido_escanio and posicion <= escanio:
                candidatos_ganadores.append((distrito, partido, posicion, nombre))
                print(f'{contador} - {distrito} - {partido} - {posicion} - {nombre}')
                contador += 1

    return candidatos_ganadores


# Modifica la estructura de diccionario en lista de listas a lista de tuplas
def transformar_lista(resultados):
    lista_transformada = []
    print("*************** Distrito - Partido - Escanios ***************")
    for distrito_dict in resultados:
        distrito = distrito_dict[0]
        partidos_escanios = distrito_dict[1:]

        for partido_escanios in partidos_escanios:
            for partido, escanios in partido_escanios.items():
                if escanios > 0:
                    lista_transformada.append((distrito, partido, escanios))
                    print(f'{distrito} - {partido} - {escanios}')

    return lista_transformada


def calcular_cocientes_dhondt(resultados_comicios, escanios):
    # Crear una lista para almacenar los distritos
    resultados_finales = []

    for i in range(0, len(resultados_comicios), 2):
        distrito = resultados_comicios[i]
        votos_partidos = resultados_comicios[i + 1]
        escanios_distrito = escanios[distrito]
        cocientes_dhondt = {}  # Crea un diccionario para almacenar los partidos(key) cocientes de D'Hondt(value)

        for partido in votos_partidos.keys():
            cocientes_dhondt[partido] = []  # Inicializa una lista para guardar todos los cocientes de D'Hondt

        while escanios_distrito > 0:

            for partido in votos_partidos.keys():
                cociente = votos_partidos[partido] / (len(cocientes_dhondt[partido]) + 1)
                cocientes_dhondt[partido].append(cociente)  # Agrega el cociente a la lista de cocientes

            escanios_distrito -= 1

        resultado_distrito = [distrito, cocientes_dhondt]
        resultados_finales.append(resultado_distrito)
        # print(f'{distrito} - {cocientes_dhondt}')

    return resultados_finales


def asignar_escanios(resultados_cocientes, escanios_por_distrito):
    resultados_finales = []

    for distrito, cocientes_dhondt in resultados_cocientes:
        escanios_distrito = escanios_por_distrito.get(distrito, 0)
        escanios_por_partido = {}  # Diccionario para almacenar los escaños asignados a cada partido

        for partido in cocientes_dhondt.keys():
            escanios_por_partido[partido] = 0  # Inicializa los escaños en 0 para cada partido

        while escanios_distrito > 0:
            max_partido = None
            max_cociente = 0

            for partido, lista_cocientes in cocientes_dhondt.items():
                if lista_cocientes:  # Verifica si la lista de cocientes no está vacía
                    cociente = max(lista_cocientes)  # Obtener el cociente más alto
                    if cociente > max_cociente:
                        max_cociente = cociente
                        max_partido = partido

            if max_partido is not None:  # Verifica si el partido no es nulo (None) antes de asignar un escaño
                escanios_por_partido[max_partido] += 1
                cocientes_dhondt[max_partido].remove(max_cociente)  # Eliminar el cociente más alto
                escanios_distrito -= 1

        resultado_distrito = [distrito, {}]  # Crea una lista para almacenar los resultados del distrito
        for partido, escanios in escanios_por_partido.items():
            resultado_distrito[1][partido] = escanios

        resultados_finales.append(resultado_distrito)
        # print(f'{distrito} - {escanios_por_partido}')

    return resultados_finales


def asignar_votos_aleatorios(lista_base, electores):
    resultados_finales = []
    # print("Distrito : Partido - Votos (generados aleatoriamente)")
    for item in lista_base:
        if isinstance(item, str):  # Comprueba si el elemento es una cadena (nombre de la provincia)
            distrito = item
            partidos = lista_base[lista_base.index(item) + 1]
            total_electores = electores.get(distrito, 0)
            votos_asignados = {}

            for partido, votos in partidos.items():
                if total_electores > 0:
                    # Asigna un número aleatorio de votos entre 0 y el número de electores disponibles
                    votos_asignados[partido] = random.randint(total_electores//10, total_electores)
                    total_electores -= votos_asignados[partido]
                    # print(f'{distrito} : {partido} - {votos_asignados[partido]}')
                else:
                    votos_asignados[partido] = 0

            resultados_finales.append(distrito)
            resultados_finales.append(votos_asignados)
    # print(resultados_finales)

    return resultados_finales


def imprimir_resultados(resultados_finales):
    for provincia, diccionario_key_value in resultados_finales:
        print(provincia)
        print(diccionario_key_value)


def main():
    resultados_prueba = asignar_votos_aleatorios(resultados_votos, electores_por_distrito)
    total_votos_por_distrito = sumar_votos_por_distrito(resultados_prueba)
    comparacion_votos_electores(total_votos_por_distrito, electores_por_distrito)
    cocientes_dhondt = calcular_cocientes_dhondt(resultados_prueba, escanios_por_distrito)
    escanios_por_partido = asignar_escanios(cocientes_dhondt, escanios_por_distrito)
    escanios = transformar_lista(escanios_por_partido)
    candidatos = leer_archivo_csv(archivo)
    obtener_candidatos_ganadores(candidatos, escanios)


if __name__ == '__main__':
    main()
