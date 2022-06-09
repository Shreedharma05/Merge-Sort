#Helper Function
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

#Merge Sort Function
def merge_sort(mylist):
    if len(mylist) == 1:
        return mylist
    mid = int(len(mylist)/2)
    left = mylist[:mid]
    right = mylist[mid:]
    return merge(merge_sort(left),merge_sort(right))

print(merge_sort([2,7,3,1,5]))
