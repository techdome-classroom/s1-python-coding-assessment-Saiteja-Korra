# def decode_message( s: str, p: str) -> bool:
#         dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
#         dp[0][0] = True  
#         for j in range(1, len(p) + 1):
#                 if p[j - 1] == '*':
#                         dp[0][j] = dp[0][j - 1]
        
#         for i in range(1, len(s) + 1):
#                 for j in range(1, len(p) + 1):
#                         if p[j - 1] == '*':
#                                 dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
#                         elif p[j - 1] == '?':
#                                 dp[i][j] = dp[i - 1][j - 1]
#                         else:
#                                 dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        
#         return dp[len(s)][len(p)]
# write your code here

def decode_message(s: str, p: str) -> bool:
    s_len, p_len = len(s), len(p)
    s_ptr = p_ptr = 0
    star_idx = s_tmp_idx = -1
    
    while s_ptr < s_len:
        # Match single character or '?'
        if p_ptr < p_len and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
            s_ptr += 1
            p_ptr += 1
        # Match '*' with any sequence of characters
        elif p_ptr < p_len and p[p_ptr] == '*':
            star_idx = p_ptr
            s_tmp_idx = s_ptr
            p_ptr += 1
        # If previous character was '*', try next character in 's'
        elif star_idx != -1:
            p_ptr = star_idx + 1
            s_tmp_idx += 1
            s_ptr = s_tmp_idx
        else:
            return False
    while p_ptr < p_len and p[p_ptr] == '*':
        p_ptr += 1
    
    return p_ptr == p_len
