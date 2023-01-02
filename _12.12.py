
#Задание 6: Проверка имени
#Надо спросить имя человека. Проверь чтобы в имени были только буквы.
#Отобрази приветствие, используя имя с большой буквы.
#Посчитай сколько букв в имени. Найти количество гласных и согласных букв с слове.
#Выведи на экран буквы имени в алфавитном порядке.(если буква встречается несколько раз, то повторять ее не надо)
name=input(str("Write your name "))
if name.isalpha() == True:
   print("Hello",name.title())
else:
    print("All characters are not alphabets")
    name=input(str("Write your name "))
print("In your name is ",len(name),"letters")
vowels = set("aeiouy")
print("Гласныъ",sum(letter in vowels for letter in name)
)  
print("Согласных",len(name)-sum(letter in vowels for letter in name)
)
name=list(name)
name.sort()
name[:] = list(set(name))
print(name)    

#Задание 5:
#На входе имеем список строк разной длины.
#На входе имеем список строк разной длины.
def all_eq(lst):
    max_item = max(lst, key=lambda x: len(x))
    max_len = len(max_item)
    return [item.ljust(max_len, '_') for item in lst]

# Тесты
print(all_eq(['крот', 'белка', 'выхухоль']))
print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))

#Задание 4: Сортировка
#Требуется создать программу, которая сортирует список чисел по убыванию/возрастанию их абсолютного значения.
from random import randint
our_list = [randint(1, 100) for i in range(randint(6, 15))]  # рандомное заполнение списка числами от 1 до 100
print(*our_list)
our_list.sort()
print("Kasvav list ",our_list)
our_list.sort(reverse=True)
print("Kakavev list", our_list)
#Задание 3: Бесполезные числа
#Николай задумался о поиске «бесполезного» числа на основании списка.
#Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, а затем делит его на длину списка и заменяет его в списке результатом деления.
#Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи в реализации такой функции.
from random import randint
 
our_list = [randint(1, 100) for i in range(randint(6, 15))]  # рандомное заполнение списка числами от 1 до 100
print(*our_list)
max=our_list [0]

for i in range (1,len(our_list)):
    if our_list[i]> max:
        max=our_list[i]
print("Suurim on  ", max)
print("Listis on ",len(our_list), "elementi")
b=int(round(max/(len(our_list))))
print (max,"/",len(our_list),"=",b)
index=our_list.index(max)
our_list[index]=b
print(our_list)

#or
def useless(lst):
    return max(lst) / len(lst)
print(useless([1, 5, 77]))
print(useless([19, 8.3, -4, 11, 0, 5]))
print(useless([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))

#Задание 2: Перемена мест
#Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.
arr = list(map(int, input('Введите некоторое количество целых чисел через пробел: ').split()))
# Например: Введите некоторое количество целых чисел через пробел: 1 2 3 4 5 6 7
print(arr)  # [1, 2, 3, 4, 5, 6, 7]
k = -1 # индекс последнего элемента списка при первой итераци
c=int(input("Сколько элементов поменять?"))
for i in range(0,c):
    #print("\nбыло - ", i, arr)
    arr[k], arr[i] = arr[i], arr[k]
    k -= 1
print("стало    ", arr)

#Задание 1: Почтовый индекс
#В Эстонии почтовые индексы состоят из 5 чисел, где первое число обозначает уезд:
#1 – Tallinn
#2 – Narva, Narva-Jõesuu
#3 – Kohtla-Järve
#4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa
#5 – Tartu linn
#6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa
#7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa
#8 – Pärnumaa
#9 – Läänemaa, Hiiumaa, Saaremaa
#Напишите программу, которая проверяет введенный индекс(количество символов, соответствие типу данных и т. д.) и отображает уезд, к которому он относится.
#Для проверки какому уезду принадлежит индекс, надо проверить первую цифру введенного значения. Для этого введеный индекс надо преобразовать в список при помощи indeks_list=list(indeks) и взять только первый элемент для проверки indeks_list[0].
#И если почтовый индеск Нарвы, Таллинна и Кохтла-Ярве, то сообщить пользователю "Оставайтесь дома!", в остальных случаях "Носите 
indeks=""
n=0
#indeks=input("Kirjuta oma indeks >> ")
while type(indeks)!=int or n!=5:
    try:
        indeks=int(input("Indeks: "))
        n=len(str(indeks))
    except :
        print("Vale indeks")
indeks_list=list(str(indeks))
maakond=["Tallinn,","Narva, Narva-Jõesuu" ,"Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
indeks_list[0]
print (maakond[int(indeks_list[0])-1])






nimi=input("Mis on sinu nimi?: ")
tahed=list(nimi)
n=len(tahed)
print(f"{n} tahed: {tahed}")
t=input("Sisesta taht, mis on vaja kustutada>> ")
nt=tahed.count(t)
j=0
if nt==0:
    print(f" {t}ei ole listis")
else:
    for i in range(len(tahed)):
        if tahed[i-j]==t:
          tahed.pop(i-j)
          j+=1
    print(f" {t}ei ole listis, on jaanud {tahed}")
t=input("Mis taht vaja otsida? >> ")
print(f"Taht {t} seisab {tahed.index(t)+1} positsioonil ")