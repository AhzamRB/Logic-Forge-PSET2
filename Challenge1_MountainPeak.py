import time

def count_ways_to_summit(n):
    if n <= 1:
        return n
    
    #For two ways: 1 step or 2 steps
    first = 1
    second = 1

    #Start from step 2 to n
    for _ in range(2, n + 1):
        current = first + second
        first = second
        second = current

    return second


n = int(input("Enter the number of steps to the mountain peak: "))

start_time = time.perf_counter()
ways = count_ways_to_summit(n)
end_time = time.perf_counter()

elapsed_time = end_time - start_time

#It asked for number of ways and not the actual paths.
print(f"For {n} steps, there are {ways} distinct ways to reach the mountain peak.")
print(f"Time taken to compute: {elapsed_time:.10f} seconds")
