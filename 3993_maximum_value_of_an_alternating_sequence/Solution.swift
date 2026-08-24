// LeetCode 3993 - Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/


class Solution {
    func maximumValue(_ n: Int, _ s: Int, _ m: Int) -> Int {
        if n == 1 { return s }
        return s + (n / 2) * (m - 1) + 1
    }
}
