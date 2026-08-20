// LeetCode 1480 - Running Sum of 1d Array
// https://leetcode.com/problems/running-sum-of-1d-array/

class Solution {
    func runningSum(_ nums: [Int]) -> [Int] {
        var nums = nums
        for i in 1..<nums.count { nums[i] += nums[i - 1] }
        return nums
    }
}
