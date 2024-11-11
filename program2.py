def decode_message( s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True  # Empty pattern matches empty string
    
    # Initialize first row for patterns starting with '*'
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
    
    return dp[len(s)][len(p)]
# write your code here