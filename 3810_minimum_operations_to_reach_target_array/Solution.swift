// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

class Solution {
    func minOperations(_ nums: [Int], _ target: [Int]) -> Int {
        var s = Set<Int>()
        for i in 0..<nums.count {
            if nums[i] != target[i] { s.insert(nums[i]) }
        }
        return s.count
    }
}
