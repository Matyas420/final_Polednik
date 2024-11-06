#1. Pole ve kterém je 5 stringovým hodnot
ovoce = ["jablko", "hruška", "banán", "mango", "ananas"]
print(ovoce)

#2. Uloží do pole hodnotu "vítr"
ovoce.append("vítr")
print(ovoce)

#3. Odstranění druhého prvnku z pole
ovoce.remove("hruška")
print(ovoce)

#4. Zamění 5 hodnotu v poli za "slunce"
ovoce[4] = "slunce"
print(ovoce)

#5. Přidání 2 stringových hodnot pomocí druhého pole
zelenina = ["brambor", "mrkev"]
ovoce.extend(zelenina)
print(ovoce)

#6. ↑
