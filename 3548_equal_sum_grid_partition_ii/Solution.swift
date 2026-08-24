// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

class Solution {
    func rotate(_ grid: [[Int]]) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        var t = Array(repeating: Array(repeating: 0, count: m), count: n)
        for i in 0..<m { for j in 0..<n { t[j][i] = grid[i][j] } }
        return t
    }

    func check(_ g: [[Int]]) -> Bool {
        let m = g.count, n = g[0].count
        var s1 = 0, s2 = 0
        var cnt1 = [Int: Int]()
        var cnt2 = [Int: Int]()
        for row in g {
            for x in row {
                s2 += x
                cnt2[x, default: 0] += 1
            }
        }
        for i in 0..<(m - 1) {
            for x in g[i] {
                s1 += x; s2 -= x
                cnt1[x, default: 0] += 1
                cnt2[x, default: 0] -= 1
            }
            if s1 == s2 { return true }
            if s1 < s2 {
                let diff = s2 - s1
                if (cnt2[diff] ?? 0) > 0 {
                    if (m - i - 1 > 1 && n > 1) ||
                        (i == m - 2 && (g[i + 1][0] == diff || g[i + 1][n - 1] == diff)) ||
                        (n == 1 && (g[i + 1][0] == diff || g[m - 1][0] == diff)) {
                        return true
                    }
                }
            } else {
                let diff = s1 - s2
                if (cnt1[diff] ?? 0) > 0 {
                    if (i + 1 > 1 && n > 1) ||
                        (i == 0 && (g[0][0] == diff || g[0][n - 1] == diff)) ||
                        (n == 1 && (g[0][0] == diff || g[i][0] == diff)) {
                        return true
                    }
                }
            }
        }
        return false
    }

    func canPartitionGrid(_ grid: [[Int]]) -> Bool {
        return check(grid) || check(rotate(grid))
    }
}
