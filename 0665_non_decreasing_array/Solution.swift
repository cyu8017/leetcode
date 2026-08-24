// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

class Solution {
    func checkPossibility(_ nums: [Int]) -> Bool {
        var nums = nums
        var changed = false
        for i in 1..<nums.count {
            if nums[i] >= nums[i - 1] { continue }
            if changed { return false }
            changed = true
            if i >= 2 && nums[i] < nums[i - 2] {
                nums[i] = nums[i - 1]
            } else {
                nums[i - 1] = nums[i]
            }
        }
        return true
    }
}
