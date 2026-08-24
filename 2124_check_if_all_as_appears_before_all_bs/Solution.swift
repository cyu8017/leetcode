// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution {
    func checkString(_ s: String) -> Bool {
        var seenB = false
        for c in s {
            if c == "b" { seenB = true }
            else if seenB { return false }
        }
        return true
    }
}
