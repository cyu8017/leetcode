// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution {
    func maximumElementAfterDecrementingAndRearranging(_ arr: [Int]) -> Int {
        var nums = arr.sorted()
        nums[0] = 1
        for i in 1..<nums.count {
            nums[i] = min(nums[i], nums[i - 1] + 1)
        }
        return nums.max()!
    }
}
