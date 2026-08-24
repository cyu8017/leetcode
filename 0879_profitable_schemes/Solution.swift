// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

class Solution {
    func profitableSchemes(_ n: Int, _ minProfit: Int, _ group: [Int], _ profit: [Int]) -> Int {
        let mod = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: minProfit + 1), count: n + 1)
        dp[0][0] = 1
        for i in 0..<group.count {
            let members = group[i], p = profit[i]
            for people in stride(from: n, through: members, by: -1) {
                for prof in stride(from: minProfit, through: 0, by: -1) {
                    let np = min(minProfit, prof + p)
                    dp[people][np] = (dp[people][np] + dp[people - members][prof]) % mod
                }
            }
        }
        var ans = 0
        for people in 0...n { ans = (ans + dp[people][minProfit]) % mod }
        return ans
    }
}
