// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

class Solution {
    func findMinimumTime(_ strength: [Int]) -> Int {
        let n = strength.count
        let N = 1 << n
        let inf = Int(1e18)
        var dp = Array(repeating: inf, count: N)
        dp[0] = 0
        let k = 1
        for mask in 0..<N {
            if dp[mask] == inf { continue }
            var opened = 0, xmask = mask
            while xmask > 0 { opened += xmask & 1; xmask >>= 1 }
            let x = 1 + opened * k
            for i in 0..<n where (mask & (1 << i)) == 0 {
                let t = (strength[i] + x - 1) / x
                let nmask = mask | (1 << i)
                if dp[mask] + t < dp[nmask] { dp[nmask] = dp[mask] + t }
            }
        }
        return dp[N - 1]
    }
}
