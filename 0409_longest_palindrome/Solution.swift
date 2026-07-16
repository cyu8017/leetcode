// LeetCode 0409 - Longest Palindrome
// https://leetcode.com/problems/longest-palindrome/

class Solution {
    func longestPalindrome(_ s: String) -> Int {
        var counts: [Character: Int] = [:]
        for char in s {
            counts[char, default: 0] += 1
        }

        var length = 0
        var odd = false
        for count in counts.values {
            length += (count / 2) * 2
            if count % 2 == 1 {
                odd = true
            }
        }

        return length + (odd ? 1 : 0)
    }
}
