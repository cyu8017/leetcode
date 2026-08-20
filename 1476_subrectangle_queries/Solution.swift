// LeetCode 1476 - Subrectangle Queries
// https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries {
    private var rectangle: [[Int]]

    init(_ rectangle: [[Int]]) { self.rectangle = rectangle }

    func updateSubrectangle(_ row1: Int, _ col1: Int, _ row2: Int, _ col2: Int, _ newValue: Int) {
        for r in row1...row2 {
            for c in col1...col2 { rectangle[r][c] = newValue }
        }
    }

    func getValue(_ row: Int, _ col: Int) -> Int { rectangle[row][col] }
}
