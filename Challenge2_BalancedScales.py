import time

def can_balance_scales(arr):

    total_sum = sum(arr)

    #cant split if odd
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    
    #We start with 0.
    possible_sums = {0}
    
    for numbers in arr:

        current_sums = set()

        for sumsum in possible_sums:

            new_sum = sumsum + numbers

            if new_sum <= target:
                current_sums.add(new_sum)
        
        #Add the new sums to the collection of possible sums
        possible_sums.update(current_sums)
        
        if target in possible_sums:
            return True
            
    return False


arr1 = [1, 5, 11, 5]

start_time = time.perf_counter()
print(f"\nArr1: {can_balance_scales(arr1)}") 
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time taken to compute: {elapsed_time:.10f} seconds\n")

arr2 = [1, 3, 5]

start_time = time.perf_counter()
print(f"Arr2: {can_balance_scales(arr2)}")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time taken to compute: {elapsed_time:.10f} seconds\n")

arr3 = [1, 6, 4, 3] #Got this example cause it wouldnt work with previous logic

start_time = time.perf_counter()
print(f"Arr3: {can_balance_scales(arr3)}")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time taken to compute: {elapsed_time:.10f} seconds\n")