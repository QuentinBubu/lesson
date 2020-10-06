# 1
mon_tuple = (5,8,6,9)

a = mon_tuple[2]

# 2
mon_tuple = (5,8,6,9)

a = mon_tuple[1]

# 3
mon_tuple = ("le", "monde", "bonjour")
print(mon_tuple[2] + " " + mon_tuple[0] + " " + mon_tuple[1] + "!")

# 4
def add(a, b):
    c = a+b
    return (a, b, c)

mon_tuple = add(5, 8)
print(f"{mon_tuple[0]} + {mon_tuple[1]} = {mon_tuple[2]}")

# 6
a,b,c,d = (5, 8, 6, 9)

# 7
ma_liste = [5, 8, 6, 9]
ma_variable = ma_liste[2]

# 8
ma_liste = [5, 8, 6, 9]
ma_liste[2] = 15

# 9
ma_liste = [5, 8, 6, 9]
ma_liste.append(15)

# 10
ma_liste = [5, 8, 6, 9]
del ma_liste[1]

# 11
ma_liste = [5, 8, 6, 9]
len(ma_liste)

# 12
ma_liste = [5, 8, 6, 9]
for element in ma_liste:
    print(element)
    
# 13
for element in range(0, 5):
    print(element)
    
# 14
ma_liste = []
for element in range(0, 5):
    ma_liste.append(element)
    
# 15
ma_liste = [p for p in range(0,5)]

# 16
l = [1, 7, 9, 15, 5, 20, 10, 8]
ma_liste = [p for p in l if p>10]

# 17
li = [1, 7, 9, 15, 5, 20, 10, 8]
ma_liste = [p**2 for p in li if p<10]

# 18
m = [
    [1, 3, 4],
    [5, 6, 8],
    [2, 1,3],
    [7, 8, 15]
]

a = m[1][2]

# 19
m = [1, 2, 3]
mm = [m, m, m]

m[0] = 100

# 20
m = [
     [1, 3, 4],
     [5, 6, 8],
     [2, 1, 3],
     [7, 8, 15]
]

nb_colonne = 3
nb_ligne = 4

for i in range(0, nb_ligne):
    for j in range(0, nb_colonne):
        a = m[i][j]
        print(a)

# 21
m = [
     [1, 3, 4],
     [5, 6, 8],
     [2, 1, 3],
     [7, 8, 15]
]

for i in range(0, len(m)):
    for j in range(0, len(m[0])):
        a = m[i][j]
        print(a)