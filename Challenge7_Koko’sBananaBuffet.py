def calculate_minimum_speed(piles, k):
    left = 1
    right = max(piles)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid  #ceiling division
        
        if hours <= k:
            answer = mid        #speed possible
            right = mid - 1     #try slowing down
        else:
            left = mid + 1      #need more speed
    
    return answer



#Example 1
piles1 = [5, 10, 3]
k1 = 4
print(f"Speed: {calculate_minimum_speed(piles1, k1)} Bananas/Hour")

#Example 2
piles2 = [5, 10, 15, 20]
k2 = 7
print(f"Speed: {calculate_minimum_speed(piles2, k2)} Bananas/Hour")