# Session 05: Longest Substring Problems
# This file covers sliding window problems on strings.
#
# Example Problem: Longest Substring Without Repeating Characters (LeetCode 3)
# Given a string s, find the length of the longest substring without repeating characters.

def length_of_longest_substring(s):
    char_map = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
            
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len

if __name__ == "__main__":
    s = "abcabcbb"
    print(f"String: {s}")
    print(f"Length of longest substring without repeating chars: {length_of_longest_substring(s)}")
