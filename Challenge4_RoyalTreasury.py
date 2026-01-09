def count_payment_combinations(coins, total_sum):

    ways = [0] * (total_sum + 1)
    
    #Base Case: Choose no coins
    ways[0] = 1
    
    for coin in coins:
        for amount in range(coin, total_sum + 1):

            ways[amount] += ways[amount - coin]
            
    return ways[total_sum]

print(f"Case A: {count_payment_combinations([1, 2, 3], 4)}")
print(f"Case B: {count_payment_combinations([2, 5, 3, 6], 10)}")
print(f"Case C: {count_payment_combinations([4], 5)}")