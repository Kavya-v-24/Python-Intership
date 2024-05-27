arr=[int(x) for x in input ("enter the sorted list of numbers separeted by space:").split()]
target=int(input("enter the target value to search:"))

start,end=0,len(arr) -1
found=False
while start<=end:
    mid=(start+end)//2
    if arr[mid]==target:
        print(f"target{target} found at index {mid}.")
        found=True
        break
    elif arr[mid]<target:
        start=mid+1
    else:
        end=mid-1
if not found:
    print(f"target {target} not found in the array.")
        