# Ejercicios con Set
# 1. Creando un set
st = set()

# 2. Creando un Set con corchetes {}
fruit = {'banana', 'orange', 'mango', 'lemon'}
print(st)

# 3. Uso de len() en set
print(len(fruit))

# 4. Checando un elemento en set utilizando el operador in
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits )

# 5. agregando elemento con add()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

# 6. Agregar elementos multiples con update()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# 7. Removiendo elementos de set con remove()
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)

# 8. Rmoviendo elementos con pop(), eliminara elementos de manera random
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)

# 9. Limpiando set con clear
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)

# 10. eliminando set con del
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# 11. Convirtiendo set a lista y viceversa
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

# 12 unir set con union() o update()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# 13 Encontrando intersepciones 
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)

# 14 Checando si un conjunto tiene subset o super set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

# 15 Checando la diferencia entre dos sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))

# 16 Encontrando la diferencia simetrica entre dos set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

# 17 Unir Sets
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))

# EJERCICIOS
# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1 encuentra len en it_companies
print(len(it_companies))

# 2 agrega "Twiter" a it_companies
it_companies.add("Twitter")
print(it_companies)

# 3 inserta multiples IT companies al set it_companies
it_companies_two = {"acer", "SalesPad", "duck duck", "blackcat"}
it_companies.update(it_companies_two)
print(it_companies)

# 4 remueve una de la compañias de it_companies
it_companies.remove("acer")
print(it_companies)

# 5 cual es la diferencia entre remove y discard
# remove elimina el elemento seleccionado pero si no lo encuentra manda un mensaje de error
# mientras discard tambien elimina el elemento seleccionado pero si no lo encuentra no manda ningun error solo el mensaje none

it_companies.discard("HP")
print(it_companies)