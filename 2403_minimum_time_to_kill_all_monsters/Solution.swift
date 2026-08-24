// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

class Solution {
    func minimumTime(_ power: [Int]) -> Int {
        let n = power.count
        let N = 1 << n
        var dp = [Int](repeating: Int.max / 4, count: N)
        dp[0] = 0
        for mask in 0..<N {
            let gain = mask.nonzeroBitCount + 1
            for i in 0..<n where (mask & (1 << i)) == 0 {
                let need = (power[i] + gain - 1) / gain
                let nm = mask | (1 << i)
                dp[nm] = min(dp[nm], dp[mask] + need)
            }
        }
        return dp[N - 1]
    }
}
