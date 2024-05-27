arr=input("enter the list of numbers separated by space:").split()
arr=[int(x) for x in arr]

target=int(input("enter the target value to search"))

found=False
for i in range(len(arr)):
    if arr[i]==target:
        print(f"target{target} found at index {i}.")
        found=True
        break
if not found:
    print(f"target{target} not found in the array.")