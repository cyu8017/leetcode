// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

class Solution {
    func canMakeEqual(_ nums: [Int], _ k: Int) -> Bool {
        return check(nums, nums[0], k) || check(nums, -nums[0], k)
    }

    func check(_ nums: [Int], _ target: Int, _ kk: Int) -> Bool {
        var cnt = 0, sign = 1
        if nums.count > 1 {
            for i in 0..<(nums.count - 1) {
                let x = nums[i] * sign
                if x == target { sign = 1 }
                else { sign = -1; cnt += 1 }
            }
        }
        return cnt <= kk && nums[nums.count - 1] * sign == target
    }
}
