// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

class Solution {
    func largestMagicSquare(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        let cols = grid[0].count
        var rowPrefix = Array(repeating: [Int](repeating: 0, count: cols + 1), count: rows)
        var colPrefix = Array(repeating: [Int](repeating: 0, count: rows + 1), count: cols)

        for i in 0..<rows {
            for j in 0..<cols {
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j]
                colPrefix[j][i + 1] = colPrefix[j][i] + grid[i][j]
            }
        }

        func rowSum(_ row: Int, _ colStart: Int, _ colEnd: Int) -> Int {
            rowPrefix[row][colEnd + 1] - rowPrefix[row][colStart]
        }

        func colSum(_ col: Int, _ rowStart: Int, _ rowEnd: Int) -> Int {
            colPrefix[col][rowEnd + 1] - colPrefix[col][rowStart]
        }

        func isMagic(_ rowStart: Int, _ colStart: Int, _ size: Int) -> Bool {
            let target = rowSum(rowStart, colStart, colStart + size - 1)
            for row in rowStart..<(rowStart + size) {
                if rowSum(row, colStart, colStart + size - 1) != target {
                    return false
                }
            }
            for col in colStart..<(colStart + size) {
                if colSum(col, rowStart, rowStart + size - 1) != target {
                    return false
                }
            }
            var diag1 = 0
            var diag2 = 0
            for offset in 0..<size {
                diag1 += grid[rowStart + offset][colStart + offset]
                diag2 += grid[rowStart + offset][colStart + size - 1 - offset]
            }
            return diag1 == target && diag2 == target
        }

        for size in stride(from: min(rows, cols), through: 1, by: -1) {
            for rowStart in 0...(rows - size) {
                for colStart in 0...(cols - size) {
                    if isMagic(rowStart, colStart, size) {
                        return size
                    }
                }
            }
        }
        return 1
    }
}
