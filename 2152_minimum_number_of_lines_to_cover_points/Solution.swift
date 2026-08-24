// LeetCode 2152 - Minimum Number of Lines to Cover Points
// https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

class Solution {
    func minimumLines(_ points: [[Int]]) -> Int {
        let n = points.count
        if n <= 2 { return 1 }
        let inf = n
        var dp = [Int](repeating: inf, count: 1 << n)
        dp[0] = 0
        for mask in 0..<(1 << n) {
            if dp[mask] == inf { continue }
            var i = 0
            while i < n && (mask & (1 << i)) != 0 { i += 1 }
            if i == n { continue }
            var nm = mask | (1 << i)
            dp[nm] = min(dp[nm], dp[mask] + 1)
            for j in (i + 1)..<n where (mask & (1 << j)) == 0 {
                nm = mask | (1 << i) | (1 << j)
                for k in 0..<n {
                    if (nm & (1 << k)) == 0 && colinear(points[i], points[j], points[k]) {
                        nm |= 1 << k
                    }
                }
                dp[nm] = min(dp[nm], dp[mask] + 1)
            }
        }
        return dp[(1 << n) - 1]
    }

    private func colinear(_ a: [Int], _ b: [Int], _ c: [Int]) -> Bool {
        return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])
    }
}
