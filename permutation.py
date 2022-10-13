def my_combinations(seq, number):
    result = []
    if number> len(seq):
        return result
    
    if number == 1:
        for i in seq:
            result.append((i,))
            
    elif number>1:
        for i in range(len(seq) -number +1):
            for j in my_combinations(seq[i+1:], number-1):
                result.append((seq[i],)+j)
    
    return result

from itertools import combinations
test = [1, 2, 3, 4]

assert set(combinations(test, 2)) == set(my_combinations(test, 2)) \
   and set(combinations(test, 3)) == set(my_combinations(test, 3))
print("통과") 