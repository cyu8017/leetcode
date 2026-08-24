// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

class Solution {
    func findPaths(_ m: Int, _ n: Int, _ maxMove: Int, _ startRow: Int, _ startColumn: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: n), count: m)
        dp[startRow][startColumn] = 1
        var result = 0
        let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for _ in 0..<maxMove {
            var nxt = Array(repeating: Array(repeating: 0, count: n), count: m)
            for row in 0..<m {
                for col in 0..<n {
                    let ways = dp[row][col]
                    if ways == 0 { continue }
                    for (dr, dc) in dirs {
                        let nr = row + dr
                        let nc = col + dc
                        if nr >= 0 && nr < m && nc >= 0 && nc < n {
                            nxt[nr][nc] = (nxt[nr][nc] + ways) % MOD
                        } else {
                            result = (result + ways) % MOD
                        }
                    }
                }
            }
            dp = nxt
        }
        return result
    }
}
