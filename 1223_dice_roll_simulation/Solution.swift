// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

class Solution {
    func dieSimulator(_ n: Int, _ rollMax: [Int]) -> Int {
        let MOD = 1_000_000_007
        var dp = [[Int]](repeating: [Int](repeating: 0, count: 6), count: n + 1)
        for j in 0..<6 { dp[1][j] = 1 }
        for i in 2...n {
            for j in 0..<6 {
                var total = 0
                for k in 0..<6 { total = (total + dp[i - 1][k]) % MOD }
                var invalid = 0
                if i - rollMax[j] - 1 > 0 {
                    for k in 0..<6 where k != j {
                        invalid = (invalid + dp[i - rollMax[j] - 1][k]) % MOD
                    }
                } else if i - rollMax[j] - 1 == 0 {
                    invalid = 1
                }
                dp[i][j] = (total - invalid + MOD) % MOD
            }
        }
        return dp[n].reduce(0) { ($0 + $1) % MOD }
    }
}
