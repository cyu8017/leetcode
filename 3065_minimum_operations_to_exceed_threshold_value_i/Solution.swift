// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        for x in nums where x < k { ans += 1 }
        return ans
    }
}
