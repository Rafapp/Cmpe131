def sort_list(list):
    n = len(list)
    i = 0
    while(i < n):
        j = 0
        while(j < n-i-1):
            if(list[j] > list[j+1]):
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
            j += 1
        i += 1
    return list

test = [4,6,7,8,3,4,2,5,8,3,1,4,7,8,0,4,6]
print(sort_list(test))