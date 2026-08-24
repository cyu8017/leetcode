// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

class Solution {
    func minimumOperations(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        let INF = 1 << 29
        var f = Array(repeating: Array(repeating: INF, count: 10), count: n)
        for i in 0..<n {
            var cnt = Array(repeating: 0, count: 10)
            for j in 0..<m { cnt[grid[j][i]] += 1 }
            if i == 0 {
                for j in 0..<10 { f[i][j] = m - cnt[j] }
            } else {
                for j in 0..<10 {
                    for k in 0..<10 where j != k {
                        f[i][j] = min(f[i][j], f[i - 1][k] + m - cnt[j])
                    }
                }
            }
        }
        return f[n - 1].min()!
    }
}
