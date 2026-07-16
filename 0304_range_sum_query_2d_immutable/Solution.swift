// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix {
    private var prefix: [[Int]]

    init(_ matrix: [[Int]]) {
        let rows = matrix.count
        let cols = rows == 0 ? 0 : matrix[0].count
        prefix = Array(repeating: Array(repeating: 0, count: cols + 1), count: rows + 1)
        for row in 0..<rows {
            for col in 0..<cols {
                prefix[row + 1][col + 1] = matrix[row][col]
                    + prefix[row][col + 1]
                    + prefix[row + 1][col]
                    - prefix[row][col]
            }
        }
    }

    func sumRegion(_ row1: Int, _ col1: Int, _ row2: Int, _ col2: Int) -> Int {
        let topLeft = prefix[row1][col1]
        let topRight = prefix[row1][col2 + 1]
        let bottomLeft = prefix[row2 + 1][col1]
        let bottomRight = prefix[row2 + 1][col2 + 1]
        return bottomRight - topRight - bottomLeft + topLeft
    }
}
