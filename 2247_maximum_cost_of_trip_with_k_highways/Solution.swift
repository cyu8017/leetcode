// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

class Solution {
    func maximumCost(_ n: Int, _ highways: [[Int]], _ k: Int) -> Int {
        if k + 1 > n { return -1 }
        var g = [[(Int, Int)]](repeating: [], count: n)
        for h in highways {
            g[h[0]].append((h[1], h[2]))
            g[h[1]].append((h[0], h[2]))
        }
        var dp = [[Int]](repeating: [Int](repeating: -1, count: n), count: 1 << n)
        for i in 0..<n { dp[1 << i][i] = 0 }
        var ans = -1
        for mask in 0..<(1 << n) {
            let cities = mask.nonzeroBitCount
            for u in 0..<n {
                if dp[mask][u] < 0 { continue }
                if cities - 1 == k { ans = max(ans, dp[mask][u]) }
                for (v, w) in g[u] {
                    if (mask & (1 << v)) != 0 { continue }
                    let nm = mask | (1 << v)
                    dp[nm][v] = max(dp[nm][v], dp[mask][u] + w)
                }
            }
        }
        return ans
    }
}
