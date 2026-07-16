// LeetCode 0348 - Design Tic-Tac-Toe
// https://leetcode.com/problems/design-tic-tac-toe/

class TicTacToe {
    private let n: Int
    private var rows: [Int]
    private var cols: [Int]
    private var diag = 0
    private var antiDiag = 0

    init(_ n: Int) {
        self.n = n
        self.rows = Array(repeating: 0, count: n)
        self.cols = Array(repeating: 0, count: n)
    }

    func move(_ row: Int, _ col: Int, _ player: Int) -> Int {
        let add = player == 1 ? 1 : -1

        rows[row] += add
        cols[col] += add
        if row == col {
            diag += add
        }
        if row + col == n - 1 {
            antiDiag += add
        }

        if abs(rows[row]) == n || abs(cols[col]) == n || abs(diag) == n || abs(antiDiag) == n {
            return player
        }

        return 0
    }
}
