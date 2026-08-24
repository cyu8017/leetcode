// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

class Solution {
    func minimumCost(_ nums: [Int], _ cost: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pn = Array(repeating: 0, count: n + 1)
        var pc = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            pn[i + 1] = pn[i] + nums[i]
            pc[i + 1] = pc[i] + cost[i]
        }
        let inf = 1 << 62
        var dp = Array(repeating: inf, count: n + 1)
        dp[n] = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in i..<n {
                let cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1]
                if cand < dp[i] { dp[i] = cand }
            }
        }
        return dp[0]
    }
}
