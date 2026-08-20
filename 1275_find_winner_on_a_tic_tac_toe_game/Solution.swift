// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution {
    func tictactoe(_ moves: [[Int]]) -> String {
        var board = [[Int]](repeating: [Int](repeating: 0, count: 3), count: 3)
        for (i, m) in moves.enumerated() {
            board[m[0]][m[1]] = i % 2 == 0 ? 1 : 2
        }
        func win(_ p: Int) -> Bool {
            for i in 0..<3 {
                if board[i].allSatisfy({ $0 == p }) { return true }
                if (0..<3).allSatisfy({ board[$0][i] == p }) { return true }
            }
            if (0..<3).allSatisfy({ board[$0][$0] == p }) { return true }
            if (0..<3).allSatisfy({ board[$0][2 - $0] == p }) { return true }
            return false
        }
        if win(1) { return "A" }
        if win(2) { return "B" }
        return moves.count == 9 ? "Draw" : "Pending"
    }
}
