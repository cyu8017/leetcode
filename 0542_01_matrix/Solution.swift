// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

class Solution {
    func updateMatrix(_ mat: [[Int]]) -> [[Int]] {
        let rows = mat.count
        let cols = mat[0].count
        var dist = Array(repeating: Array(repeating: 1_000_000_000, count: cols), count: rows)
        var queue: [(Int, Int)] = []

        for row in 0..<rows {
            for col in 0..<cols {
                if mat[row][col] == 0 {
                    dist[row][col] = 0
                    queue.append((row, col))
                }
            }
        }

        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var head = 0
        while head < queue.count {
            let (row, col) = queue[head]
            head += 1
            for (dr, dc) in directions {
                let nr = row + dr
                let nc = col + dc
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols {
                    let candidate = dist[row][col] + 1
                    if dist[nr][nc] > candidate {
                        dist[nr][nc] = candidate
                        queue.append((nr, nc))
                    }
                }
            }
        }

        return dist
    }
}
