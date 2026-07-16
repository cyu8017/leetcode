// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

class Solution {
    func wallsAndGates(_ rooms: inout [[Int]]) {
        guard !rooms.isEmpty else { return }
        let rows = rooms.count
        let cols = rooms[0].count
        var queue: [(Int, Int)] = []
        for row in 0..<rows {
            for col in 0..<cols {
                if rooms[row][col] == 0 {
                    queue.append((row, col))
                }
            }
        }
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while !queue.isEmpty {
            let (row, col) = queue.removeFirst()
            for (dr, dc) in directions {
                let nr = row + dr
                let nc = col + dc
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols && rooms[nr][nc] == Int.max {
                    rooms[nr][nc] = rooms[row][col] + 1
                    queue.append((nr, nc))
                }
            }
        }
    }
}
