// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

class Solution {
    func countCells(_ grid: [[Character]], _ pattern: String) -> Int {
        let m = grid.count, n = grid[0].count
        var row: [Character] = []
        var col: [Character] = []
        for i in 0..<m { for j in 0..<n { row.append(grid[i][j]) } }
        for j in 0..<n { for i in 0..<m { col.append(grid[i][j]) } }
        var hMark = Array(repeating: Array(repeating: false, count: n), count: m)
        var vMark = Array(repeating: Array(repeating: false, count: n), count: m)
        let pat = Array(pattern)
        let plen = pat.count
        if plen > 0 && row.count >= plen {
            for i in 0...(row.count - plen) {
                if Array(row[i..<(i + plen)]) == pat {
                    for t in 0..<plen {
                        let pos = i + t
                        hMark[pos / n][pos % n] = true
                    }
                }
            }
        }
        if plen > 0 && col.count >= plen {
            for i in 0...(col.count - plen) {
                if Array(col[i..<(i + plen)]) == pat {
                    for t in 0..<plen {
                        let pos = i + t
                        vMark[pos % m][pos / m] = true
                    }
                }
            }
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n where hMark[i][j] && vMark[i][j] { ans += 1 }
        }
        return ans
    }
}
