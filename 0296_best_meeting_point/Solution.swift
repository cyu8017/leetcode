// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

class Solution {
    func minTotalDistance(_ grid: [[Int]]) -> Int {
        var rows: [Int] = []
        var cols: [Int] = []
        for rowIndex in 0..<grid.count {
            for colIndex in 0..<grid[rowIndex].count {
                if grid[rowIndex][colIndex] == 1 {
                    rows.append(rowIndex)
                    cols.append(colIndex)
                }
            }
        }
        cols.sort()
        let rowMedian = rows[rows.count / 2]
        let colMedian = cols[cols.count / 2]
        var total = 0
        for row in rows {
            total += abs(row - rowMedian)
        }
        for col in cols {
            total += abs(col - colMedian)
        }
        return total
    }
}
