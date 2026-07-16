// LeetCode 0125 - Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

func isPalindrome(s string) bool {
    left,right := 0,len(s)-1
    alnum := func(c byte) bool { return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || c >= '0' && c <= '9' }
    lower := func(c byte) byte { if c >= 'A' && c <= 'Z' { return c + 32 }; return c }
    for left < right { for left < right && !alnum(s[left]) { left++ }; for left < right && !alnum(s[right]) { right-- }; if lower(s[left]) != lower(s[right]) { return false }; left++; right-- }
    return true
}