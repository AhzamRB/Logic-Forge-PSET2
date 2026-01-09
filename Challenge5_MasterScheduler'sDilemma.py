def min_cancelled_bookings(intervals):

    intervals.sort(key=lambda x: x[1])  #Sort by ending time as [[0, 1], [0, 1], ...]
    
    kept = 0
    last_end = 0
    
    for start, end in intervals:
        if start >= last_end:
            kept += 1
            last_end = end
    
    return len(intervals) - kept


intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
intervals2 = [[1, 3], [1, 3], [1, 3]]
intervals3 = [[1, 2], [5, 10], [18, 35]]

print(f"Number of cancelled bookings for intervals1 = {min_cancelled_bookings(intervals1)}")
print(f"Number of cancelled bookings for intervals2 = {min_cancelled_bookings(intervals2)}")
print(f"Number of cancelled bookings for intervals3 = {min_cancelled_bookings(intervals3)}")