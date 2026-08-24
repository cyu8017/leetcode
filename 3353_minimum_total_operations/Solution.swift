// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var ops = 0
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            if nums[i] != nums[i + 1] { ops += 1 }
        }
        return ops
    }
}
