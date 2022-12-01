from collections import defaultdict, Counter

map = defaultdict(int)

data = [1,3,1,5,2,3,2,2,7]

# count the freq of the elements using dictionary

for d in data:
    map[d] +=1
print(map)

# count using counter
counter = Counter(data)
print(counter)