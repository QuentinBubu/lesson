import math

dicoTouches = {
    'a': (0,0),
    'z': (1,0),
    'e': (2,0),
    'r': (3,0),
    't': (4,0),
    'y': (5,0),
    'u': (6,0),
    'i': (7,0),
    'o': (8,0),
    'p': (9,0),
    
    'q': (0,1),
    's': (1,1),
    'd': (2,1),
    'f': (3,1),
    'g': (4,1),
    'h': (5,1),
    'j': (6,1),
    'k': (7,1),
    'l': (8,1),
    'm': (9,1),
    
    'w': (0,2),
    'x': (1,2),
    'c': (2,2),
    'v': (3,2),
    'b': (4,2),
    'n': (5,2),
    
    ' ': (0,3),
    'shift': (-1,2),
    '<': (-0.5,2),
    '>': (-1.5,2),
    ',': (6,2),
    'é': (1,-1),
    'è': (8,-1),
    'à': (9,-1),
    '&': (0,-1),
    '(': (4,-1),
    ')': (10,-1),
    
    '7': (17,0),
    '8': (18,0),
    '9': (19,0),
    '4': (17,1),
    '5': (18,1),
    '6': (19,1),
    '1': (17,2),
    '2': (18,2),
    '3': (19,2),
    '0': (17,3)
}

def toucheVersCoord(touche):
    return dicoTouches[touche]
"""
def distanceClavier(touche1, touche2):
    distance = (
        abs(toucheVersCoord(touche1.lower())[0] - toucheVersCoord(touche2.lower())[0]),
        abs(toucheVersCoord(touche1.lower())[1] - toucheVersCoord(touche2.lower())[1])
    )
    distanceFinale = math.sqrt(distance[0]**2 + distance[1]**2)
    return distanceFinale
"""

def distanceClavier(touche1, touche2): # +
    distance = [
        abs(toucheVersCoord(touche1.lower())[0] - toucheVersCoord(touche2.lower())[0]),
        abs(toucheVersCoord(touche1.lower())[1] - toucheVersCoord(touche2.lower())[1])
    ]
    
    if touche1.isupper():
        distance[0] += toucheVersCoord('shift')[0]
        distance[1] += toucheVersCoord('shift')[1]
    
    distanceFinale = math.sqrt(distance[0]**2 + distance[1]**2)
    return distanceFinale

def distance_mot(mot):
    distance = 0
    for i in range(len(mot)-1):
        distance += distanceClavier(mot[i], mot[i+1])
    return distance

def distance_phrase(phrase):
    distance = 0
    for i in range(len(phrase)-1):
        distance += distanceClavier(phrase[i], phrase[i+1])
    return distance