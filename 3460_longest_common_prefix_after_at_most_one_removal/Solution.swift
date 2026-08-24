// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

class Solution {
    func longestCommonPrefix(_ s: String, _ t: String) -> Int {
        let sa = Array(s), ta = Array(t)
        var i = 0, j = 0
        var removed = false
        while i < sa.count && j < ta.count {
            if sa[i] == ta[j] {
                i += 1; j += 1
                continue
            }
            if removed { break }
            removed = true
            i += 1
        }
        return j
    }
}
