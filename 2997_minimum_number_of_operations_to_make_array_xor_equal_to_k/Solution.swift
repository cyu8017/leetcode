// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var xorr = 0
        for v in nums { xorr ^= v }
        return (xorr ^ k).nonzeroBitCount
    }
}
