def is_armstrong(num):
    original_num=num
    armstrong_sum=0
    num_digits=len(str(num))
    while num>0:
        digit=num%10
        armstrong_sum+=digit**num_digits
        num//=10
    return original_num==armstrong_sum
result=is_armstrong(153)
print(result)