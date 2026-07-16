// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

class Solution {
    func isValidSudoku(_ board: [[Character]]) -> Bool {
        var rows = Array(repeating: Set<Character>(), count: 9)
        var cols = Array(repeating: Set<Character>(), count: 9)
        var boxes = Array(repeating: Set<Character>(), count: 9)

        for r in 0..<9 {
            for c in 0..<9 {
                let value = board[r][c]
                if value == "." {
                    continue
                }

                let box = (r / 3) * 3 + c / 3
                if rows[r].contains(value) || cols[c].contains(value) || boxes[box].contains(value) {
                    return false
                }

                rows[r].insert(value)
                cols[c].insert(value)
                boxes[box].insert(value)
            }
        }

        return true
    }
}
