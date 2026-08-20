// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution {
    func isPrefixString(_ s: String, _ words: [String]) -> Bool {
        var built = ""
        for w in words {
            built += w
            if built == s { return true }
            if built.count > s.count || !s.hasPrefix(built) { return false }
        }
        return false
    }
}
