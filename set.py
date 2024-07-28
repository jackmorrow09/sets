set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}

print(set1)
print(set2)

#union- it joins two sets

print(set1.union(set2))

#intersection- it returns the items which are found in both sets
print(set1.intersection(set2))

#diference- presecence of items in one set but not the other
print(set1.difference(set2))

print(set2.difference(set1))

#symmetric- it gives you the items that are not found in both sets
print(set1.symmetric_difference(set2))

#sets are not indexable
#print(set1[3])

for i in set1:
    print(i)

#adding items to the set
set1.add(6)
print(set1)

#removing items from a set
set1.remove(5)
print(set1)

#check if item is present in the list or not
if 4 in set1:
    print("yes")

else:
    print("no")