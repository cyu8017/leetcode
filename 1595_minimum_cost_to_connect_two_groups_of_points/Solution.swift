// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

class Solution {
    func connectTwoGroups(_ cost: [[Int]]) -> Int {
        let m = cost.count, n = cost[0].count
        let full = 1 << n
        let inf = Int.max / 4
        var dp = Array(repeating: inf, count: full)
        dp[0] = 0
        for row in cost {
            var nxt = Array(repeating: inf, count: full)
            for mask in 0..<full {
                for j in 0..<n {
                    let value = row[j]
                    let newMask = mask | (1 << j)
                    nxt[newMask] = min(nxt[newMask], dp[mask] + value, nxt[mask] + value)
                }
            }
            dp = nxt
        }
        let minimum = (0..<n).map { j in (0..<m).map { cost[$0][j] }.min()! }
        var ans = inf
        for mask in 0..<full {
            var extra = 0
            for j in 0..<n where (mask >> j) & 1 == 0 {
                extra += minimum[j]
            }
            ans = min(ans, dp[mask] + extra)
        }
        return ans
    }
}
