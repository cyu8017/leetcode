// LeetCode 1328 - Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

class Solution {
    func breakPalindrome(_ palindrome: String) -> String {
        var chars = Array(palindrome)
        if chars.count == 1 { return "" }
        for i in 0..<(chars.count / 2) {
            if chars[i] != "a" {
                chars[i] = "a"
                return String(chars)
            }
        }
        chars[chars.count - 1] = "b"
        return String(chars)
    }
}
