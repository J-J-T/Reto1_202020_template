"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1



def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    lst = loadCSVFile("theMoviesdb/movies-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMovies()

            elif int(inputs[0])==2: #opcion 2
                pass

            elif int(inputs[0])==3: #opcion 3
                pass

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
#Requisito 3- Conocer un repositorio
def conocer_un_director(casting,datails):
    casting_por_director = lt.newList('SINGLE_LINKED', None)
    director = input("Ingrese el director\n")
    t1_start = process_time()

    iter = listiterator.newIterator(casting)
    while listiterator.hasNext(iter):
        c = listiterator.next(iter)
        if c["director_name"] == director:
            lt.addFirst(casting_por_director, c)

    peliculas_director=lt.newList('SINGLE_LINKED', None)
    iter = listiterator.newIterator(casting_por_director)
    while listiterator.hasNext(iter):
        c= listiterator.next(iter)
        iter1= listiterator.newIterator(details)
        while listiterator.hasNext(iter1):
            d= listiterator.next(iter1)
            if c["id"]==d["id"]:
                lt.addFirst(peliculas_director,d)
    print("Película, Director, vote_average, vote_count")
    print("-"*45)

    iter = listiterator.newIterator(peliculas_director)
    while listiterator.hasNext(iter):
        u = listiterator.next(iter)
        print((" "*5)+u['original_title']+(" "*5)+u["vote_average"]+(" "*5)+u["vote_count"])

    numero_de_peliculas_director = lt.size(peliculas_director)
    suma_vote_average = 0.0

    iter = listiterator.newIterator(peliculas_director)
    while listiterator.hasNext(iter):
        u = listiterator.next(iter)
        suma_vote_average = suma_vote_average + float(u["vote_average"])

    promedio_peliculas = 0
    if(numero_de_peliculas_director > 0):
        promedio_peliculas = suma_vote_average/numero_de_peliculas_director

    print("Número de peliculas: ",numero_de_peliculas_director)
    print("Promedio de votos: ",suma_vote_average)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")





#Requisito 4- Conocer un actor
def conocer_un_actor(casting,datails):

    casting_por_actor = lt.newList('SINGLE_LINKED', None)
    actor = input("Ingrese el actor\n")

    t1_start = process_time()

    iter = listiterator.newIterator(casting)
    while listiterator.hasNext(iter):
        c = listiterator.next(iter)
        if (c['actor1_name'] == actor) or (c['actor2_name'] == actor) or (c['actor3_name'] == actor) or (c['actor4_name'] == actor) or (c['actor5_name'] == actor):
            lt.addFirst(casting_por_actor, c)
    peliculas_actor=lt.newList('SINGLE_LINKED', None)
    direc=lt.newList('SINGLE_LINKED', None)
    iter = listiterator.newIterator(casting_por_actor)
    while listiterator.hasNext(iter):
        c= listiterator.next(iter)
        iter1= listiterator.newIterator(details)
        while listiterator.hasNext(iter1):
            d= listiterator.next(iter1)
            if c["id"]==d["id"]:
                lt.addFirst(peliculas_actor,d)
                lt.addFirst(direc,c)
    print("Película, vote_average")
    print("-"*30)

    iter = listiterator.newIterator(peliculas_actor)
    while listiterator.hasNext(iter):
        u = listiterator.next(iter)
        print((" "*5)+u['original_title']+(" "*5)+u["vote_average"])

    numero_de_peliculas_actor = lt.size(peliculas_actor)
    suma_vote_average = 0.0

    iter = listiterator.newIterator(peliculas_actor)
    while listiterator.hasNext(iter):
        u = listiterator.next(iter)
        suma_vote_average = suma_vote_average + float(u["vote_average"])

    promedio_peliculas = 0
    if(numero_de_peliculas_actor > 0):
        promedio_peliculas = suma_vote_average/numero_de_peliculas_actor

    print("Número de peliculas: ",numero_de_peliculas_actor)
    print("Promedio de votos: ",suma_vote_average)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
if __name__ == "__main__":
    main()
