// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution {
    func allCellsDistOrder(_ rows: Int, _ cols: Int, _ rCenter: Int, _ cCenter: Int) -> [[Int]] {
        var cells = [[Int]]()
        for r in 0..<rows {
            for c in 0..<cols {
                cells.append([r, c])
            }
        }
        cells.sort { abs($0[0] - rCenter) + abs($0[1] - cCenter) < abs($1[0] - rCenter) + abs($1[1] - cCenter) }
        return cells
    }
}
