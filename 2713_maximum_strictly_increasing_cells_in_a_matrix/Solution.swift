// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

class Solution {
    func maxIncreasingCells(_ mat: [[Int]]) -> Int {
        let m = mat.count, n = mat[0].count
        var cells: [(Int, Int, Int)] = []
        for i in 0..<m {
            for j in 0..<n { cells.append((mat[i][j], i, j)) }
        }
        cells.sort { $0.0 < $1.0 }
        var rowMax = Array(repeating: 0, count: m)
        var colMax = Array(repeating: 0, count: n)
        var dp = Array(repeating: Array(repeating: 0, count: n), count: m)
        var ans = 0
        var i = 0
        while i < cells.count {
            var j = i
            while j < cells.count && cells[j].0 == cells[i].0 { j += 1 }
            var buf: [(Int, Int, Int)] = []
            for k in i..<j {
                let r = cells[k].1, c = cells[k].2
                let best = max(rowMax[r], colMax[c])
                dp[r][c] = best + 1
                ans = max(ans, dp[r][c])
                buf.append((r, c, dp[r][c]))
            }
            for b in buf {
                rowMax[b.0] = max(rowMax[b.0], b.2)
                colMax[b.1] = max(colMax[b.1], b.2)
            }
            i = j
        }
        return ans
    }
}
