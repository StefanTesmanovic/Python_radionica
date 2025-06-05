import copy

original = [[1, 2], [3, 4]]

# Shallow copy – kopira samo spoljašnju listu, ne i unutrašnje
shallow = copy.copy(original)
shallow.append([5, 6]) 

# Deep copy – koristimo za matrice ili složene strukture podataka
deep = copy.deepcopy(original)


shallow[0][0] = 999
original[0].append(6)
original.append([7, 8]) 

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
