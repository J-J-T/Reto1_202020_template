import config as conf
import csv
from ADT import list as lt
from DataStructures import listiterator
from time import process_time 

details = lt.newList('SINGLE_LINKED', None)
# details_file = "Data/AllMoviesDetailsCleaned.csv" 
details_file = "Data/SmallMoviesDetailsCleaned.csv"
with open(details_file, encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        lt.addFirst(details, row)



print("5- Req 5 - Entender un genero cinematografico")

#2) Filtrar

details_genero = lt.newList('SINGLE_LINKED', None)

genero = input("Ingrese el nombre del genero\n")

t1_start = process_time()

iter = listiterator.newIterator(details)
while listiterator.hasNext(iter):
    c = listiterator.next(iter)
    if genero in c["genres"]:
        lt.addFirst(details_genero, c)
        


lista_peliculas=lt.addLast("ARRAY_LIST",None)
numero_de_peliculas_genero = lt.size(details_genero)
suma_vote_average = 0.0

iter = listiterator.newIterator(details_genero)
while listiterator.hasNext(iter):
    u = listiterator.next(iter)
    lt.addLast(lista_peliculas,u["original_title"])
    suma_vote_average = suma_vote_average + float(u["vote_average"])

promedio_peliculas = 0
if(numero_de_peliculas_director > 0):
    promedio_peliculas = suma_vote_average/numero_de_peliculas_director


print(lista_peliculas["elements"])
print("Numero de peliculas de ese genero" + str(numero_de_peliculas_genero))
print("Promedio vote_average: " + str(promedio_peliculas))

t1_stop = process_time() #tiempo final
print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

