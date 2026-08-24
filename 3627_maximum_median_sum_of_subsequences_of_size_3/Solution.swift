// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

class Solution {
    func maximumMedianSum(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var ans = 0
        var i = n / 3
        while i < n {
            ans += nums[i]
            i += 2
        }
        return ans
    }
}
