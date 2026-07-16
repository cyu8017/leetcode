// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

class Solution {
    private let directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    func updateBoard(_ board: [[Character]], _ click: [Int]) -> [[Character]] {
        var grid = board
        let rows = grid.count
        let cols = grid[0].count
        let row = click[0]
        let col = click[1]

        if grid[row][col] == "M" {
            grid[row][col] = "X"
            return grid
        }

        reveal(&grid, row, col, rows, cols)
        return grid
    }

    private func countMines(_ board: [[Character]], _ r: Int, _ c: Int, _ rows: Int, _ cols: Int) -> Int {
        var total = 0
        for (dr, dc) in directions {
            let nr = r + dr
            let nc = c + dc
            if nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == "M" {
                total += 1
            }
        }
        return total
    }

    private func reveal(_ board: inout [[Character]], _ r: Int, _ c: Int, _ rows: Int, _ cols: Int) {
        guard r >= 0 && r < rows && c >= 0 && c < cols && board[r][c] == "E" else {
            return
        }
        let mines = countMines(board, r, c, rows, cols)
        if mines == 0 {
            board[r][c] = "B"
            for (dr, dc) in directions {
                reveal(&board, r + dr, c + dc, rows, cols)
            }
        } else {
            board[r][c] = Character(String(mines))
        }
    }
}
