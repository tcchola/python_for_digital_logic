# Primjer 1: Ispisati ''Hello world'' 5 puta

for i in range(5):  # 01234
    print("Hello World")

# Primjer 2: Ispisati kvadrat svakog broja između 1 i n. Broj n unosi korisnik.

n = int(input("Unesite broj: "))

for i in range(1, n + 1):
    print(pow(i, 2))

# Primjer 3. Izračunati sumu parnih brojeva između 1 i 10

sum = 0

for i in range(1, 11):
    if (i % 2 == 0):
        sum += i

print("Suma svih parnih brojeva izmedju 1 i 10 je", sum)

# Primjer 4. Ispisati sve brojeve od 10 do 1.

for i in range(10, 0, -1):
    print(i)

# Primjer 5: Ispisati sumu brojeva od 0 do 10. Na broju 7 prekinuti petlju te ispisati sumu brojeva do tog koraka.

sum = 0
steps = 0

for i in range(11):
    if (i == 7):
        break
    sum += i
    steps += 1

print("Suma brojeva od 0 do 7 je", sum)  # 0+1+2+3+4+5+6 = 21
print("Broj koraka do rjesenja je", steps)  # 7

# Primjer 1: Izračunati sumu neparnih brojeva:
# a) od 1 do 10

sum = 0
for i in range(1, 11):
    if (i % 2 != 0):
        sum += i
print("Suma neparnih brojeva od 1 do 10 je", sum)  # 1+3+5+7+9 = 25

# b) od 5 do 10

sum = 0
for i in range(5, 11):
    if (i % 2 != 0):
        sum += i
print("Suma neparnih brojeva od 5 do 11 je", sum)  # 5+7+9 = 21

# Primjer 2: Ispisati:
# a) parne brojeve od 1 do 10

for i in range(1, 11):
    if (i % 2 == 0):
        print(i)

    # b) kvadrate brojeva od 1 do 10

for i in range(1, 11):
    print(pow(i, 2))

# Primjer 3: Napisati program gdje će poruku i broj njenog ponavljanja unijeti korisnik.

poruka = input("Unesite poruku: ")
brPonavljanja = int(input("Koliko puta zelite da se ispise?: "))

for i in range(brPonavljanja):
    print(poruka)

# Primjer 4: Izračunati proizvod brojeva od x do y. Korisnik unosi vrijednosti za x i za y, pr. od x=1, y=10

x = int(input("X: "))
y = int(input("Y: "))

# x=abs(x)
# y=abs(y)

while (x > y):
    x = int(input("X: "))
    y = int(input("Y: "))

proizvod = 1

for i in range(x, y + 1):
    proizvod *= i

print("Proizvod brojeva od", x, "do", y, "je", proizvod)  # u sustini faktorijel

# Primjer 5: Ispisati brojeve u rangu od 1 do 10, djeljivi sa 5.

for i in range(1, 11):
    if (i % 5 == 0):
        print(i)