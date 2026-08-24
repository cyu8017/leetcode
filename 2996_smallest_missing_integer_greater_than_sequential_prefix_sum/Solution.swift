// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

class Solution {
    func missingInteger(_ nums: [Int]) -> Int {
        var sum = nums[0]
        var i = 1
        while i < nums.count && nums[i] == nums[i - 1] + 1 {
            sum += nums[i]
            i += 1
        }
        let seen = Set(nums)
        while seen.contains(sum) { sum += 1 }
        return sum
    }
}
