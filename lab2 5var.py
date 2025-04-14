
def find_all_indexes(input_str, search_str):
    l1 = [] 
    length = len(input_str) 
    index = 0 
    while index < length:
        i = input_str.find(search_str, index) 
    if i == -1: 
        return l1 
    l1.append(i) 
    index = i + 1 
    return l1 
s = 'abaacdaa12aa2' 
print(find_all_indexes(s, 'a')) 
print(find_all_indexes(s, 'aa'))


def BinarySearch(s, t):
    first = 0
    last = len(s)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if s[mid] == t:
            index = mid
        else:
            if t<s[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
s='GATATATGCATATACTT'
t='atat'
BinarySearch (s,t)