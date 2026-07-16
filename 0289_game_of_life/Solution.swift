// LeetCode 0289 - Game of Life
// https://leetcode.com/problems/game-of-life/

class Solution {
    func gameOfLife(_ board: inout [[Int]]) {
        let rows = board.count
        let cols = board[0].count
        for row in 0..<rows {
            for col in 0..<cols {
                var liveNeighbors = 0
                for dr in -1...1 {
                    for dc in -1...1 {
                        if dr == 0 && dc == 0 {
                            continue
                        }
                        let nr = row + dr
                        let nc = col + dc
                        if nr >= 0 && nr < rows && nc >= 0 && nc < cols && (board[nr][nc] & 1) == 1 {
                            liveNeighbors += 1
                        }
                    }
                }
                if (board[row][col] & 1) == 1 && (liveNeighbors == 2 || liveNeighbors == 3) {
                    board[row][col] |= 2
                } else if (board[row][col] & 1) == 0 && liveNeighbors == 3 {
                    board[row][col] |= 2
                }
            }
        }
        for row in 0..<rows {
            for col in 0..<cols {
                board[row][col] >>= 1
            }
        }
    }
}
