// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution {
    func countPalindromicSubsequence(_ s: String) -> Int {
        let chars = Array(s)
        var first: [Character: Int] = [:]
        var last: [Character: Int] = [:]
        for (i, c) in chars.enumerated() {
            if first[c] == nil { first[c] = i }
            last[c] = i
        }
        var ans = 0
        for c in first.keys {
            let f = first[c]!, l = last[c]!
            if l - f > 1 {
                ans += Set(chars[(f + 1)..<l]).count
            }
        }
        return ans
    }
}
