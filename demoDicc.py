#DICCIONARIO

usuario = {
    "nombre" : "Nicolás Ferix Moreyra",
    "edad" : 25,
    "contacto" : "nicolas_ferix@hotmail.com",
    "numDNI" : 40203557
}



#ACCEDER A UN VALOR

print(usuario["edad"])



#ACTUALIZAR UN VALOR O AGREGAR UN PAR

#Actualizar
usuario["contacto"] = "nicolas.ferix.m@gmail.com"

#Agregar
usuario["nacimiento"] = "04/11/1997"
print(usuario)



#METODOS


#copy y fromkeys

#copy
usuarioCopia = usuario.copy()
print(usuarioCopia)

print(usuario == usuarioCopia) #relacional --> True
print(usuarioCopia is usuario) #identidad --> False (Porque es una copia,devuelve un diccionario difernete)


#fromkeys (inicializamos un diccionario con el mismo valor y diferentes claves)
nuevoDict = dict.fromkeys ((494916,88941,384321,18949873,5474556,4423445,995646,6480029,796432), "Usuario") #"hola" es una secuencia
print(nuevoDict)




#get (pedimos una clave y si no la encuentra devuelve un valor por defecto, evitando el error)

#error
#print(usuario[87983687984]) 

#get
print(usuario.get(87983687984,"Valor no encontrado")) 
print(usuario.get("nombre","Valor no encontrado"))



#items, keys , values (Devuelven iterables para el ciclo For)

#.items() hace una lista de tuplas de cada par del dic.
for clave, valor in usuario.items():
    print(f"{clave} : {valor}")

print(usuario.items())

#.keys() Hace una lista de las claves
for clave in usuario.keys():
    print(f" - {clave}")

print(usuario.keys())

#.values() Hace una lista de los valores
for valor in usuario.values():
    print(f" - {valor}")

print(usuario.values())




#setdefault y update

#.setdefault() (Si la clave no existe crea una nueva clave con ese valor. Si la clave existe, permanece el valor que tenía antes)
nuevoValor = usuario.setdefault("nombre", "Esteban Gimenez")
print(f"Valor : {nuevoValor}")

print(usuario)


#.update() Sería algo así como concatenar diccionarios. Agrega nuevos pares
masDatos = {
    "domicilio" : "Espinillo",
    "numero" : 66,
    "CP" : 5149,
    "edad" : 26,
    "contacto" : "nicolas_ferix@hotmail.com"
}

usuario.update(masDatos)
print(usuario)



# clear (Le borra todo)

usuarioCopia.clear()
print(usuarioCopia)



#popitem , pop

#.popitem() (Elimina el último par agregado y también devuelve ese valor)
print(usuario.popitem())

#.pop() (Hay que darle una clave. Devuelve el valor)
print(usuario.pop("domicilio"))



#len (Devuelve la cantidad de pares que tiene el diccionario)

print(usuario)
print(len(usuario))



#del<<elemento>> (Destruye - borra un elemento por completo. Pasar una clave NO ES UNA BUENA PRÁCTICA)

del usuario["numero"] 
print(usuario)

# del usuario
# print(usuario) La borra completamente. Le quita su espacio en la memoria RAM




#DESAFIO

#Una persona lleva un registro de los distintos precios
#que ofrecen para un mismo producto en distintos comercios.
#Los datos que tenemos son: El kg de papa esta a $300 , $250 y $380.
#La yerba esta a $200 , $210 y $200. Y el pan a $120, $100 y $150.
#Teniendo en cuenta estos datos, mostrarle al usuario esta informacion de
#manera amigable, ordenando los precios de menor a mayor.
#Formato: Precios de la papa [250, 300, 380]

precios = {
    "papa" : [300 , 250, 380],
    "yerba" : [200 , 210, 200],
    "pan" : [120, 100, 150]
}

for clave, valor in precios.items():
    valor.sort()
    print(f"Precios de {clave}: {valor}")

