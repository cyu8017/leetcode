// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution {
    func maximumDifference(_ nums: [Int]) -> Int {
        var ans = -1, mn = nums[0]
        for i in 1..<nums.count {
            if nums[i] > mn { ans = max(ans, nums[i] - mn) }
            else { mn = nums[i] }
        }
        return ans
    }
}
