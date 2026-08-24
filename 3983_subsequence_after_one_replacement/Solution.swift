// LeetCode 3983 - Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/


class Solution {
    func canMakeSubsequence(_ s: String, _ t: String) -> Bool {
        let s = Array(s), t = Array(t)
        let m = s.count, n = t.count
        var i0 = 0, i1 = 0, j = 0
        while i1 < m && j < n {
            if s[i1] == t[j] { i1 += 1 }
            if i1 < i0 + 1 { i1 = i0 + 1 }
            if s[i0] == t[j] { i0 += 1 }
            j += 1
        }
        return i1 == m
    }
}
