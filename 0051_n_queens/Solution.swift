// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

class Solution {
    func solveNQueens(_ n: Int) -> [[String]] {
        var result: [[String]] = []
        var cols = Set<Int>()
        var diag1 = Set<Int>()
        var diag2 = Set<Int>()
        var board = Array(repeating: String(repeating: ".", count: n), count: n)

        func backtrack(_ row: Int) {
            if row == n {
                result.append(board)
                return
            }

            for col in 0..<n {
                if cols.contains(col) || diag1.contains(row + col) || diag2.contains(row - col) {
                    continue
                }

                cols.insert(col)
                diag1.insert(row + col)
                diag2.insert(row - col)

                var rowChars = Array(board[row])
                rowChars[col] = "Q"
                board[row] = String(rowChars)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
                board[row] = String(repeating: ".", count: n)
            }
        }

        backtrack(0)
        return result
    }
}
