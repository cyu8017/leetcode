// LeetCode 3797 - Count Routes To Climb A Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

class Solution {
    func countRoutes(_ grid: [String], _ d: Int) -> Int {
        let MOD = 1_000_000_007
        let n = grid.count
        let m = grid[0].count
        let rows = grid.map { Array($0) }
        var upRadius = 0
        while (upRadius + 1) * (upRadius + 1) + 1 <= d * d { upRadius += 1 }
        var arrived = [Int](repeating: 0, count: m)
        for c in 0..<m {
            if rows[n - 1][c] == "." { arrived[c] = 1 }
        }
        for r in stride(from: n - 1, through: 0, by: -1) {
            var pref = [Int](repeating: 0, count: m + 1)
            for i in 0..<m { pref[i + 1] = (pref[i] + arrived[i]) % MOD }
            var horizontal = [Int](repeating: 0, count: m)
            for c in 0..<m {
                if rows[r][c] == "#" { continue }
                let l = max(0, c - d), rr = min(m - 1, c + d)
                horizontal[c] = (pref[rr + 1] - pref[l] - arrived[c]) % MOD
                if horizontal[c] < 0 { horizontal[c] += MOD }
            }
            if r == 0 {
                var ans = 0
                for c in 0..<m { ans = (ans + arrived[c] + horizontal[c]) % MOD }
                return ans
            }
            var pref2 = [Int](repeating: 0, count: m + 1)
            for c in 0..<m { pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % MOD }
            var next = [Int](repeating: 0, count: m)
            for c in 0..<m {
                if rows[r - 1][c] == "#" { continue }
                let l = max(0, c - upRadius), rr = min(m - 1, c + upRadius)
                next[c] = pref2[rr + 1] - pref2[l]
                if next[c] < 0 { next[c] += MOD }
            }
            arrived = next
        }
        return 0
    }
}
