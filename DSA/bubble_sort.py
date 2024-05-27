def bubble_sort(arr):
    n=len(arr)
    
    for i in range (n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
my_list=[67,29,74,73,66,68,86,46,56,46,65,61,6]
print("orignal list",my_list)
bubble_sort(my_list)
print("sorted list:",my_list)