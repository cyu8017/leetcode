// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution {
    func validTicTacToe(_ board: [String]) -> Bool {
        var x = 0, o = 0
        for row in board {
            for ch in row {
                if ch == "X" { x += 1 }
                else if ch == "O" { o += 1 }
            }
        }
        if o > x || x - o > 1 { return false }
        let xWin = win(board, Character("X"))
        let oWin = win(board, Character("O"))
        if xWin && oWin { return false }
        if xWin && x != o + 1 { return false }
        if oWin && x != o { return false }
        return true
    }

    private func win(_ board: [String], _ player: Character) -> Bool {
        let rows = board.map { Array($0) }
        for i in 0..<3 {
            if rows[i][0] == player && rows[i][1] == player && rows[i][2] == player { return true }
            if rows[0][i] == player && rows[1][i] == player && rows[2][i] == player { return true }
        }
        if rows[0][0] == player && rows[1][1] == player && rows[2][2] == player { return true }
        if rows[0][2] == player && rows[1][1] == player && rows[2][0] == player { return true }
        return false
    }
}
