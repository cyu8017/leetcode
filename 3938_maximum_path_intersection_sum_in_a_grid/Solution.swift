// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/


class Solution {
    func maxPathSum(_ grid: [[Int]]) -> Int {
        let rows = grid.count, cols = grid[0].count
        var answer = Int.min
        for row in 0..<rows {
            answer = max(answer, checkLine(cols) { grid[row][$0] })
        }
        for col in 0..<cols {
            answer = max(answer, checkLine(rows) { grid[$0][col] })
        }
        if rows > 2 && cols > 2 {
            for row in 1..<(rows - 1) {
                for col in 1..<(cols - 1) {
                    if grid[row][col] > answer { answer = grid[row][col] }
                }
            }
        }
        return answer
    }

    private func checkLine(_ length: Int, _ value: (Int) -> Int) -> Int {
        var answer = Int.min
        var bestEnding = value(0) + value(1)
        if bestEnding > answer { answer = bestEnding }
        if length > 2 {
            for i in 2..<length {
                if value(i - 1) + value(i) > bestEnding + value(i) {
                    bestEnding = value(i - 1) + value(i)
                } else {
                    bestEnding += value(i)
                }
                if bestEnding > answer { answer = bestEnding }
            }
        }
        return answer
    }
}
