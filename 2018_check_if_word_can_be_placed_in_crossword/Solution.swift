// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

class Solution {
    func placeWordInCrossword(_ board: [[Character]], _ word: String) -> Bool {
        let m = board.count, n = board[0].count
        let L = word.count
        let w = Array(word)
        for r in 0..<m {
            var c = 0
            while c < n {
                while c < n && board[r][c] == "#" { c += 1 }
                let start = c
                while c < n && board[r][c] != "#" { c += 1 }
                if c - start == L {
                    var cells = [Character]()
                    for i in start..<c { cells.append(board[r][i]) }
                    if match(cells, w) { return true }
                }
            }
        }
        for c in 0..<n {
            var r = 0
            while r < m {
                while r < m && board[r][c] == "#" { r += 1 }
                let start = r
                while r < m && board[r][c] != "#" { r += 1 }
                if r - start == L {
                    var cells = [Character]()
                    for i in 0..<L { cells.append(board[start + i][c]) }
                    if match(cells, w) { return true }
                }
            }
        }
        return false
    }

    private func match(_ cells: [Character], _ word: [Character]) -> Bool {
        let L = word.count
        if cells.count != L { return false }
        var ok1 = true, ok2 = true
        for i in 0..<L {
            if cells[i] != " " && cells[i] != word[i] { ok1 = false }
            if cells[i] != " " && cells[i] != word[L - 1 - i] { ok2 = false }
        }
        return ok1 || ok2
    }
}
