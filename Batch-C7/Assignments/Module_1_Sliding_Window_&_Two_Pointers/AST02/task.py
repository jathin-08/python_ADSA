def Check_Palindrome(n: int, s: str) -> bool:
    left = 0
    right = n - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            s1 = s[left+1:right+1]
            s2 = s[left:right]
            return s1 == s1[::-1] or s2 == s2[::-1]
    return True

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n,s))
