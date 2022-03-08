def sort_list(list):
    n = len(list)
    i = 0
    while(i < n):
        while(i < n - i - 1):
            if(list[i] > list[i + 1]):
                temp = list[i]
                list[i] = list[i+1] 
                list[i+1] = temp
            i += 1
        i += 1
    return list

test = [3,2,4,89]
print(sort_list(test))