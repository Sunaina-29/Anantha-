def calculate_range(real_numbers):
    n = len(real_numbers)

    if (n<3):
        return"Lists with length less than 3 not acceptable"
    max = real_numbers[0]
    min = real_numbers[0]
    for i in range(1,n):
        if (real_numbers[i]>max):
            max=real_numbers[i]
        elif (real_numbers[i]<min):
            min=real_numbers[i]

    range_value=max-min
    return range_value


real_numbers=[5,3,8,1,0,4]
result=calculate_range(real_numbers)
print(f"The range of the list is {result}")