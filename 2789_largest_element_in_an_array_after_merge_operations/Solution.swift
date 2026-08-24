// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

class Solution {
    func maxArrayValue(_ nums: [Int]) -> Int {
        var cur = nums[nums.count - 1]
        var ans = cur
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            if nums[i] <= cur { cur += nums[i] } else { cur = nums[i] }
            ans = max(ans, cur)
        }
        return ans
    }
}
