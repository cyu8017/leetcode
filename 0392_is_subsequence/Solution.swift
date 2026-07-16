// LeetCode 0392 - Is Subsequence
// https://leetcode.com/problems/is-subsequence/

class Solution {
    func isSubsequence(_ s: String, _ t: String) -> Bool {
        var index = s.startIndex
        for char in t {
            if index < s.endIndex && s[index] == char {
                index = s.index(after: index)
            }
        }
        return index == s.endIndex
    }
}
