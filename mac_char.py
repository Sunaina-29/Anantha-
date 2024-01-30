def highest_occuring_char(name):
    Occurances=0
    max_count=0
    max_char=name[0]

    n=len(name)
    for i in range(len(name)):
        Occurances = name.count(name[i])
        if (Occurances>max_count):
            max_char=name[i]
            max_count=Occurances

    return max_char,max_count

name = input("Enter a string:")
max_char1, max_count1=highest_occuring_char(name)
print(f"Highest occuring character in the input string in '{max_char1}' and it occured {max_count1} times in the string")