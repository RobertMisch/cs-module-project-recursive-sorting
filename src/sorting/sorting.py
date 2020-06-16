import math
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # print(merged_arr)
    sorting=True
    indexA=0
    indexB=0
    index_merged=0
    #so we need to compare the first element of each, and then move the index one higher on the one we store
    while sorting:
        if index_merged==len(merged_arr):
            sorting=False
            return merged_arr
        elif indexB > len(arrB)-1:
            merged_arr[index_merged]=arrA[indexA]
            indexA+=1
            index_merged+=1
        elif indexA > len(arrA)-1:
            merged_arr[index_merged]=arrB[indexB]
            indexB+=1
            index_merged+=1
        elif arrA[indexA]>arrB[indexB]:
            merged_arr[index_merged]=arrB[indexB]
            indexB+=1
            index_merged+=1
        elif arrA[indexA]<arrB[indexB]:
            merged_arr[index_merged]=arrA[indexA]
            indexA+=1
            index_merged+=1
        elif arrA[indexA]==arrB[indexB]:
            merged_arr[index_merged]=arrB[indexB]
            indexB+=1
            index_merged+=1
            merged_arr[index_merged]=arrA[indexA]
            indexA+=1
            index_merged+=1
# print(merge([1,2,3,4],[1,2,3,4]))
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #need to divide into 2 seperate arrays
    if(len(arr)>1):
        middle= math.floor(len(arr)//2)
        arrA=arr[:middle]
        arrB=arr[middle:]
        return merge(merge_sort(arrA),merge_sort(arrB))
    else:
        return arr

    # return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

