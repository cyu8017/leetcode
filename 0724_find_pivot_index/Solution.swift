// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

class Solution {
    func pivotIndex(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var left = 0
        for i in 0..<nums.count {
            if left == total - left - nums[i] { return i }
            left += nums[i]
        }
        return -1
    }
}
