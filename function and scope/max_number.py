def find_max(numbers):
    if not numbers:
        return None
    max_num=numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
list=[34,65,10,6,90]
maximum= find_max (list)
print("Maximum no is:", maximum)