// LeetCode 0063 - Unique Paths II
// https://leetcode.com/problems/unique-paths-ii/

class Solution {
    func uniquePathsWithObstacles(_ obstacleGrid: [[Int]]) -> Int {
        if obstacleGrid[0][0] == 1 {
            return 0
        }

        let rows = obstacleGrid.count
        let cols = obstacleGrid[0].count
        var row = Array(repeating: 0, count: cols)
        row[0] = 1

        for i in 0..<rows {
            if obstacleGrid[i][0] == 1 {
                row[0] = 0
            }

            for j in 1..<cols {
                if obstacleGrid[i][j] == 1 {
                    row[j] = 0
                } else {
                    row[j] += row[j - 1]
                }
            }
        }

        return row[cols - 1]
    }
}
