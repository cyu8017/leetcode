// LeetCode 1463 - Cherry Pickup II
// https://leetcode.com/problems/cherry-pickup-ii/

class Solution {
    func cherryPickup(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var dp = [0 * n + (n - 1): grid[0][0] + (n > 1 ? grid[0][n - 1] : 0)]
        for r in 1..<m {
            var nxt = [Int: Int]()
            for (key, score) in dp {
                let a = key / n, b = key % n
                for na in (a - 1)...(a + 1) {
                    for nb in (b - 1)...(b + 1) where na >= 0 && na < n && nb >= 0 && nb < n {
                        let val = score + grid[r][na] + (na != nb ? grid[r][nb] : 0)
                        let nk = na * n + nb
                        nxt[nk] = max(nxt[nk, default: -1], val)
                    }
                }
            }
            dp = nxt
        }
        return dp.values.max() ?? 0
    }
}
