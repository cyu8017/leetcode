// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

class Solution {
    func solveSudoku(_ board: inout [[Character]]) {
        var rows = Array(repeating: Set<Character>(), count: 9)
        var cols = Array(repeating: Set<Character>(), count: 9)
        var boxes = Array(repeating: Set<Character>(), count: 9)
        var empty: [(Int, Int)] = []

        for r in 0..<9 {
            for c in 0..<9 {
                let value = board[r][c]
                if value == "." {
                    empty.append((r, c))
                    continue
                }
                let box = (r / 3) * 3 + c / 3
                rows[r].insert(value)
                cols[c].insert(value)
                boxes[box].insert(value)
            }
        }

        func backtrack(_ index: Int) -> Bool {
            if index == empty.count {
                return true
            }

            let (r, c) = empty[index]
            let box = (r / 3) * 3 + c / 3
            for digit in Character("123456789") {
                if rows[r].contains(digit) || cols[c].contains(digit) || boxes[box].contains(digit) {
                    continue
                }

                board[r][c] = digit
                rows[r].insert(digit)
                cols[c].insert(digit)
                boxes[box].insert(digit)

                if backtrack(index + 1) {
                    return true
                }

                board[r][c] = "."
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box].remove(digit)
            }

            return false
        }

        _ = backtrack(0)
    }
}
