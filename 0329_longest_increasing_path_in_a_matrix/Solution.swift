// LeetCode 0329 - Longest Increasing Path in a Matrix
// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution {
    func longestIncreasingPath(_ matrix: [[Int]]) -> Int {
        guard !matrix.isEmpty && !matrix[0].isEmpty else {
            return 0
        }

        let rows = matrix.count
        let cols = matrix[0].count
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var memo: [Int: Int] = [:]

        func dfs(_ row: Int, _ col: Int) -> Int {
            let key = row * cols + col
            if let cached = memo[key] {
                return cached
            }

            var best = 1
            for (dr, dc) in directions {
                let nr = row + dr
                let nc = col + dc
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols && matrix[nr][nc] > matrix[row][col] {
                    best = max(best, 1 + dfs(nr, nc))
                }
            }
            memo[key] = best
            return best
        }

        var answer = 0
        for row in 0..<rows {
            for col in 0..<cols {
                answer = max(answer, dfs(row, col))
            }
        }
        return answer
    }
}
