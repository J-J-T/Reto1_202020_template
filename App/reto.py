import config as conf
import csv
from ADT import list as lt
from DataStructures import listiterator
from time import process_time 


# 0) Cargar archivos

casting = lt.newList('SINGLE_LINKED', None)
# casting_file = "Data/MoviesCastingRaw-small.csv" 
casting_file = "Data/MoviesCastingRaw-small.csv"
with open(casting_file, encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        lt.addFirst(casting, row)


details = lt.newList('SINGLE_LINKED', None)
# details_file = "Data/SmallMoviesDetailsCleaned.csv" 
details_file = "Data/SmallMoviesDetailsCleaned.csv"
with open(details_file, encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        lt.addFirst(details, row)
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


