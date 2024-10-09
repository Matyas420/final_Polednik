import random
#1. V poli je 9 hodnot od 0 do 100
array1 = [25, 14, 56, 32, 47, 75, 81, 96, 67]

#2. Print vypíše čísla na indexech "0, 3, 8"
print(array1[0])
print(array1[len(array1) // 2])
print(array1[-1])

#3. Zamění 5 indexovou hodnotu na 34
array1[5] = 34

#4. Vypíše číslo na hodnotě 6
print(array1[6])

#5. Vypíše délku pole
print(len(array1))

#6. Vypíše nejmenší číslo a největší číslo z pole
print(min(array1))
print(max(array1))

#7. Vytvoření druhého pole
array2 = [100, 200, 300, 400, 500, 600]

#8. Sečtení polí
print(sum(array1+array2))

#9. Sečtení indexově 1 a 5 hodnot z pole č.2
print(array2[1] + array2[5])

#Bonus shuffle automaticky zamíchá čísla v poli
random.shuffle(array2)
print(array2)
