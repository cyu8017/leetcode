// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/


class Solution {
    func countLocalMaximums(_ matrix: [[Int]]) -> Int {
        let rows = matrix.count, cols = matrix[0].count
        var positions = Array(repeating: [(Int, Int)](), count: 201)
        for row in 0..<rows {
            for col in 0..<cols {
                let value = matrix[row][col]
                if value > 0 { positions[value].append((row, col)) }
            }
        }
        var answer = 0
        for value in 1...200 {
            if positions[value].isEmpty { continue }
            var prefix = Array(repeating: Array(repeating: 0, count: cols + 1), count: rows + 1)
            for row in 0..<rows {
                for col in 0..<cols {
                    let add = matrix[row][col] > value ? 1 : 0
                    prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add
                }
            }
            for (row, col) in positions[value] {
                let top = max(0, row - value), bottom = min(rows - 1, row + value)
                let left = max(0, col - value), right = min(cols - 1, col + value)
                var greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left]
                for dr in [-value, value] {
                    for dc in [-value, value] {
                        let rr = row + dr, cc = col + dc
                        if rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value {
                            greater -= 1
                        }
                    }
                }
                if greater == 0 { answer += 1 }
            }
        }
        return answer
    }
}
