from itertools import combinations

class Ordre():
    def __init__(self, by, volum, vekt, pris):
        self.by = by
        self.volum = volum
        self.vekt = vekt
        self.pris = pris

ordre = [
    Ordre("Steinkjer", 6, 6, 16),
    Ordre("Tønsberg", 16, 5, 22),
    Ordre("Kongsvinger", 4, 5, 10),
    Ordre("Elverum", 5, 7, 14),
    Ordre("Meråker", 12, 6, 17),
    Ordre("Kongsberg", 7, 2, 19),
    Ordre("Trondheim", 10, 4, 11),
    Ordre("Lillehammer", 5, 7, 18),
    Ordre("Hamar", 13, 3, 6),
    Ordre("Oslo", 6, 5, 8),
    Ordre("Geiranger", 17, 20, 8),
    Ordre("Molde", 5, 11, 14),
    Ordre("Kristiansund", 17, 2, 11),
    Ordre("Porsgrunn", 12, 3, 19)
]

def rSubset(arr, r):
    return list(combinations(arr, r))

def create_selection():
    selection = []
    for x in range(2,9):
        subset = rSubset(ordre, x)
        selection += subset
    return selection

def check_if_possible():
    selection = create_selection()

    for subarray in selection:
        volum = 0
        pris = 0
        vekt = 0
        ordrenavn = []
        for item in subarray:
            print(item.by)
            if volum + item.volum <= 81 and vekt + item.vekt <= 30:
                volum += item.volum
                vekt += item.vekt
                pris += item.pris
                ordrenavn.append(item.by)
            else:
                break
        if pris > 116:
            print(f'Lets go! Denne turen tjener vi {pris}000,- på\nDen går fra:')
            for navn in ordrenavn:
                print(navn, end=" – ")
            print("\n")

check_if_possible()
