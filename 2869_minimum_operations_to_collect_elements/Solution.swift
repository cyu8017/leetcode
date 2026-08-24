// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var need = Set(1...k)
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            need.remove(nums[i])
            if need.isEmpty { return nums.count - i }
        }
        return nums.count
    }
}
