// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

class Solution {
    func validPalindrome(_ s: String) -> Bool {
        let chars = Array(s)
        func isPal(_ l: Int, _ r: Int) -> Bool {
            var l = l, r = r
            while l < r {
                if chars[l] != chars[r] { return false }
                l += 1; r -= 1
            }
            return true
        }
        var l = 0, r = chars.count - 1
        while l < r {
            if chars[l] != chars[r] {
                return isPal(l + 1, r) || isPal(l, r - 1)
            }
            l += 1; r -= 1
        }
        return true
    }
}
