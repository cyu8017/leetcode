// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

class Solution {
    func sortMatrix(_ grid: [[Int]]) -> [[Int]] {
        var grid = grid
        let n = grid.count
        var diags = [Int: [Int]]()
        for i in 0..<n {
            for j in 0..<n {
                diags[i - j, default: []].append(grid[i][j])
            }
        }
        for (k, var v) in diags {
            if k >= 0 { v.sort(by: >) } else { v.sort() }
            diags[k] = v
        }
        var idx = [Int: Int]()
        for i in 0..<n {
            for j in 0..<n {
                let k = i - j
                let pos = idx[k, default: 0]
                grid[i][j] = diags[k]![pos]
                idx[k] = pos + 1
            }
        }
        return grid
    }
}
