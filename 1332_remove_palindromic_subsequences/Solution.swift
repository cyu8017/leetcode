// LeetCode 1332 - Remove Palindromic Subsequences
// https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution {
    func removePalindromeSub(_ s: String) -> Int {
        if s.isEmpty { return 0 }
        return s == String(s.reversed()) ? 1 : 2
    }
}
