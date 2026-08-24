// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

class Solution {
    func possibleToStamp(_ grid: [[Int]], _ stampHeight: Int, _ stampWidth: Int) -> Bool {
        let m = grid.count, n = grid[0].count
        var pref = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: m + 1)
        for i in 0..<m {
            for j in 0..<n {
                pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j]
            }
        }
        var diff = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: m + 1)
        var i = 0
        while i + stampHeight - 1 < m {
            var j = 0
            while j + stampWidth - 1 < n {
                let sum = pref[i + stampHeight][j + stampWidth] - pref[i][j + stampWidth]
                    - pref[i + stampHeight][j] + pref[i][j]
                if sum == 0 {
                    diff[i][j] += 1
                    diff[i][j + stampWidth] -= 1
                    diff[i + stampHeight][j] -= 1
                    diff[i + stampHeight][j + stampWidth] += 1
                }
                j += 1
            }
            i += 1
        }
        var cur = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for i in 0..<m {
            for j in 0..<n {
                var v = diff[i][j]
                if i > 0 { v += cur[i - 1][j] }
                if j > 0 { v += cur[i][j - 1] }
                if i > 0 && j > 0 { v -= cur[i - 1][j - 1] }
                cur[i][j] = v
                if grid[i][j] == 0 && v == 0 { return false }
            }
        }
        return true
    }
}
