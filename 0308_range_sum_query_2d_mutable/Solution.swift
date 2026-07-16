// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix {
    private var matrix: [[Int]]
    private var rows: Int
    private var cols: Int
    private var tree: [[Int]]

    init(_ matrix: [[Int]]) {
        self.matrix = matrix
        self.rows = matrix.count
        self.cols = rows == 0 ? 0 : matrix[0].count
        self.tree = Array(repeating: Array(repeating: 0, count: cols + 1), count: rows + 1)
        for row in 0..<rows {
            for col in 0..<cols {
                add(row + 1, col + 1, matrix[row][col])
            }
        }
    }

    func update(_ row: Int, _ col: Int, _ val: Int) {
        let delta = val - matrix[row][col]
        matrix[row][col] = val
        add(row + 1, col + 1, delta)
    }

    func sumRegion(_ row1: Int, _ col1: Int, _ row2: Int, _ col2: Int) -> Int {
        return prefix(row2 + 1, col2 + 1)
            - prefix(row1, col2 + 1)
            - prefix(row2 + 1, col1)
            + prefix(row1, col1)
    }

    private func add(_ row: Int, _ col: Int, _ delta: Int) {
        var rowIndex = row
        while rowIndex <= rows {
            var colIndex = col
            while colIndex <= cols {
                tree[rowIndex][colIndex] += delta
                colIndex += colIndex & -colIndex
            }
            rowIndex += rowIndex & -rowIndex
        }
    }

    private func prefix(_ row: Int, _ col: Int) -> Int {
        var total = 0
        var rowIndex = row
        while rowIndex > 0 {
            var colIndex = col
            while colIndex > 0 {
                total += tree[rowIndex][colIndex]
                colIndex -= colIndex & -colIndex
            }
            rowIndex -= rowIndex & -rowIndex
        }
        return total
    }
}
