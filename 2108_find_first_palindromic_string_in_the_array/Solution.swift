// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution {
    func firstPalindrome(_ words: [String]) -> String {
        for w in words {
            let chars = Array(w)
            var l = 0, r = chars.count - 1, ok = true
            while l < r {
                if chars[l] != chars[r] { ok = false; break }
                l += 1; r -= 1
            }
            if ok { return w }
        }
        return ""
    }
}
