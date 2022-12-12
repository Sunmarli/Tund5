#Задание 2: Перемена мест
#Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.
list=[]
list.insert(i, x)



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