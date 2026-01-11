def find_longest_mirror_length(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    #Base case: when there is only one character
    for i in range(n):
        dp[i][i] = 1

    #Build substrings of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]: #Characters match
                dp[i][j] = 2 + dp[i + 1][j - 1] 
            else: #Characters don't match
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) 

    return dp[0][n - 1]



s1 = "bbbab" 
print(f"Length: {find_longest_mirror_length(s1)}")

s2  = "cbbd"
print(f"Length: {find_longest_mirror_length(s2)}")