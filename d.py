# Authors: Alex, Emil, Mikael
# Gruppe 11

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

def ranger(volum, vekt, pris):
    volVekt = volum + vekt
    return volVekt / pris

arrMain = []

def printCombination(arr, n, r):
	data = [0] * r
	combinationUtil(arr, data, 0, n - 1, 0, r)

def combinationUtil(arr, data, start, end, index, r):
	if index == r:
		for j in range(r):
			print(data[j], end = ", ",)
		print()
		return
        
	i = start
	while i <= end and end - i + 1 >= r - index:
		data[index] = arr[i].by
		combinationUtil(arr, data, i + 1, end, index + 1, r)
		i += 1

n = len(ordre)
for x in range(1, 9):
    printCombination(ordre, n, x)



        