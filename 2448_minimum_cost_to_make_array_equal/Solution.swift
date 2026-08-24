// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

class Solution {
    func minCost(_ nums: [Int], _ cost: [Int]) -> Int {
        let n = nums.count
        var idx = Array(0..<n)
        idx.sort { nums[$0] < nums[$1] }
        let totalCost = cost.reduce(0, +)
        var pref = 0
        var median = 0
        for i in idx {
            pref += cost[i]
            if pref * 2 >= totalCost {
                median = nums[i]
                break
            }
        }
        var ans = 0
        for i in 0..<n {
            ans += abs(nums[i] - median) * cost[i]
        }
        return ans
    }
}
