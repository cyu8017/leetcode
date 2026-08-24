// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

class Solution {
    func minOperations(_ s: String) -> Int {
        var ans = 0
        for c in s {
            if c != "a" { ans = max(ans, 26 - Int(c.asciiValue! - 97)) }
        }
        return ans
    }
}
