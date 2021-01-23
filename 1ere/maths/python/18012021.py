# ---------- FICHE N°1 ----------

# Activité 1
# 1
"""
l1 => Affect le nombre 64 à n
l2 => Affect le reste de la division de n par 10 à u soit 4
l3 => Affect le quotient entier de la division de n par 10 à d soit 6
l4 => Effectue l'opération: 10*u + d soit 10*4 + 6 et affecte le résultat à m
l5 => Affiche la variable m soit 46
"""

# 2-a
"""
10*4 + 6 = 46
"""

# 2-b
"""
l1 => Affect le nombre 41 à n
l2 => Affect le reste de la division de n par 10 à u soit 1
l3 => Affect le quotient entier de la division de n par 10 à d soit 4
l4 => Effectue l'opération: 10*u + d soit 10*1 + 4 et affecte le résultat à m
l5 => Affiche la variable m soit 14
"""

# Exercice 1
# 1
def algo(n, m):
    x = 10*n + m
    y = 100*x
    z = 100*y
    s = x + y + z
    print(locals())

algo(2, 7)
"""
{
    's': 272727,
    'z': 270000,
    'y': 2700,
    'x': 27,
    'm': 7,
    'n': 2
}
"""
# 2
algo(1, 9)
"""
{
    's': 191919,
    'z': 190000,
    'y': 1900,
    'x': 19,
    'm': 9,
    'n': 1
}
"""
"""
s est alors 3 fois la valeur de x à la suite
"""

# Exercice 2
# 1
def variable(n):
    a = n - 2
    b = a*n
    c = b + 1
    print(locals())

variable(5)
variable(3)
variable(1)
variable(4)

"""
{
    'c': 16,
    'b': 15,
    'a': 3,
    'n': 5
}
{
    'c': 4,
    'b': 3,
    'a': 1,
    'n': 3
}
{
    'c': 0,
    'b': -1,
    'a': -1,
    'n': 1
}
{
    'c': 9,
    'b': 8,
    'a': 2,
    'n': 4
}
"""

# 3
"""
c > 0
b = c - 1
n = a + 2
"""

# Exercice 3
x = 5
y = 4
z = 2*x - y
y = 2*y - 3*z
x = 5*z + y - 4*x
print(f"\nx={x}\ny={y}\nz={z}")

"""
x=0
y=-10
z=6
"""

"""
x toujours égal à 0
y toujours négatif
"""

# exercice 4
"""
1-c
2-f
3-d
4-a
5-b
6-e
"""

# Exercice 5
liste = {
    "a": 2,
    "b": 4.5,
    "c": 2 + 3.5,
    "d": 51//6,
    "e": 2.5 + 3.5,
    "f": 14/2,
    "g": "33",
    "h": 33,
    "i": 2e10,
    "j": ["u", "e", "i"]
}

for key, value in liste.items():
    print(f"{key} => {type(value)}")

"""
a => <class 'int'>
b => <class 'float'>
c => <class 'float'>
d => <class 'int'>
e => <class 'float'>
f => <class 'float'>
g => <class 'str'>
h => <class 'int'>
i => <class 'float'>
j => <class 'list'>
"""

# ---------- FICHE N°2 ----------

# Exercice 9
# 1
def essai(a, b):
    return 4*x - 2*y + 6

print(essai(1, 5)) # 26
print(essai(5, 1)) # 26

# 2
print(essai(-1, -2)) # 26

# Exercice 10
def moyenne(a, b, c):
    return (a + b + c) / 3

# Exercice 11
def temps(D, V):
    return D/V

# Exercice 12
# 1
def c_to_k(c):
    return c + 273.15

# 2
def k_to_c(k):
    return k - 273.15

# Exercice 13
# 1
def plus_grand(a, b):
    if a > b:
        pg = a
    else:
        pg = b
    return pg

print(plus_grand(5, -6)) # 5

# 2
def maximum(a, b, c, d):
    x = plus_grand(a, b) # 15
    y = plus_grand(c, d) # 9
    M = plus_grand(x, y) # 15
    return M

maximum(10, 15, 9, 8)

# Exercice 6
def g(a, b, c):
    s = a + b
    p = a*b
    d = a - b
    return (s + p - d)

# 1
# g avec 3 arguments

# 2
print(g(2, 3, 7)) # 12
print(g(1, 4, 2)) # 12

"""
i: 0, y: 6, z: 0
avec i = 0 et y = 6 jusqu'à z = 99

i: 1, y: 4, z: 0
avec i = 1 et y = 4 jusqu'à z = 99

i: 2, y: 3, z: 0
avec i = 2 et y = 3 jusqu'à z = 99

i: 4, y: 2, z: 0
avec i = 4 et y = 2 jusqu'à z = 99
i: 10, y: 1, z: 0

avec i = 10 et y = 1 jusqu'à z = 99
"""