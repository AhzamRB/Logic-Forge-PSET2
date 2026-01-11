def maximize_freelance_profit(deadlines, profits):

    #Combines deadlines and profits
    jobs = list(zip(deadlines, profits))
    max_deadline = max(deadlines)
    
    #Sorts the jobs by their profits in descending
    jobs.sort(key=lambda x: x[1], reverse=True)
    
    time_slots = [False] * (max_deadline + 1)

    total_jobs = 0
    total_profit = 0

    for deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if not time_slots[t]:  #If slot free
                time_slots[t] = True  #Mark slot as occupied
                total_profit += profit  #Add profit
                total_jobs += 1
                break 

    return [total_jobs, total_profit]


#Example 1
deadlines1 = [4, 1, 1, 1]
profits1 = [20, 10, 40, 30]
print(f"Example 1 Output: {maximize_freelance_profit(deadlines1, profits1)}") 


#Example 2
deadlines2 = [2, 1, 2, 1, 1]
profits2 = [100, 19, 27, 25, 15]
print(f"Example 2 Output: {maximize_freelance_profit(deadlines2, profits2)}") 