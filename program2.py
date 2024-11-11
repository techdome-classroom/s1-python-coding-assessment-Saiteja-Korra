
# write your code here

def decode_message(s: str, p: str) -> bool:
    s_len, p_len = len(s), len(p)
    s_ptr = p_ptr = 0
    star_idx = s_tmp_idx = -1
    
    while s_ptr < s_len:
        if p_ptr < p_len and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
            s_ptr += 1
            p_ptr += 1
        elif p_ptr < p_len and p[p_ptr] == '*':
            star_idx = p_ptr
            s_tmp_idx = s_ptr
            p_ptr += 1
        elif star_idx != -1:
            p_ptr = star_idx + 1
            s_tmp_idx += 1
            s_ptr = s_tmp_idx
        else:
            return False
    while p_ptr < p_len and p[p_ptr] == '*':
        p_ptr += 1
    
    return p_ptr == p_len
