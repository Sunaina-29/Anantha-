def count_pairs_with_sum(lst, target_sum):
    count = 0 # This variable is to count the number of pairs that sums up to the target_sum. So it is first initialized to 0
    n = len(lst)

#using 2 inner loops so that the numbers in the list don't duplicate with itself as a pair. And accessing the list elements with their indexes.
    for i in range(n):
        for j in range(i+1,n): 
                if(lst[i]+lst[j]==target_sum):
                     count+=1
    return count

my_list = [2, 7, 4, 1, 3, 6]
target_sum = 10
result = count_pairs_with_sum(my_list, target_sum)

print(f"Number of pairs with sum {target_sum}: {result}")
