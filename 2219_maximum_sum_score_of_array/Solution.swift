// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

class Solution {
    func maximumSumScore(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var pref = 0
        var ans = Int.min
        for x in nums {
            pref += x
            ans = max(ans, max(pref, total - pref + x))
        }
        return ans
    }
}
