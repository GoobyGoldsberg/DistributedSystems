# Q1: Creational Design Pattern (Prototype Design Pattern) [40 Marks]

import copy

original_list = [[1,2,3], [4,5,6]]

copy1 = copy.copy(original_list)



print("Original list: ", original_list)

for i in range(0, len(original_list[1])):
    copy1[1][i] += 10

print("\n\nShallow copy example")
print("Copy1: ", copy1)
print("Original list: ", original_list)


copy2 = copy.deepcopy(original_list)

for i in range(0, len(original_list[1])):
    copy2[1][i] -= 5
    
print("\nDeep copy example")
print("Copy2: ", copy2)
print("Original list: ", original_list)


copy3 = copy.copy(original_list)

copy3[1][0] = 111

print("\nShallow copy example")
print("Copy3: ", copy3)
print("Original list: ", original_list)


copy4 = copy.deepcopy(original_list)

copy4[1][0] = 777

print("\nDeep copy example")
print("Copy4: ", copy2)
print("Original list: ", original_list)