// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution {
    func maxStrength(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        if n == 1 { return nums[0] }
        var prod = 1
        var used = false
        var i = 0
        while i + 1 < n && nums[i] < 0 && nums[i + 1] < 0 {
            prod *= nums[i] * nums[i + 1]
            used = true
            i += 2
        }
        let negLeft = i < n && nums[i] < 0
        while i < n {
            if nums[i] > 0 {
                prod *= nums[i]
                used = true
            }
            i += 1
        }
        if !used {
            if negLeft {
                if nums.contains(0) { return 0 }
                return nums[n - 1]
            }
            return 0
        }
        return prod
    }
}
