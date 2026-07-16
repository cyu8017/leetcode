// LeetCode 0125 - Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let characters = Array(s.lowercased())
        var left = 0
        var right = characters.count - 1
        while left < right {
            while left < right && !characters[left].isLetter && !characters[left].isNumber {
                left += 1
            }
            while left < right && !characters[right].isLetter && !characters[right].isNumber {
                right -= 1
            }
            if characters[left] != characters[right] {
                return false
            }
            left += 1
            right -= 1
        }
        return true
    }
}