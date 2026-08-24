// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

class Solution {
    func findPattern(_ board: [[Int]], _ pattern: [String]) -> [Int] {
        let m = board.count, n = board[0].count
        let r = pattern.count, c = pattern[0].count
        if m - r + 1 > 0 && n - c + 1 > 0 {
            for i in 0...(m - r) {
                for j in 0...(n - c) {
                    if check(board, pattern, i, j, r, c) { return [i, j] }
                }
            }
        }
        return [-1, -1]
    }

    private func check(_ board: [[Int]], _ pattern: [String], _ i: Int, _ j: Int, _ r: Int, _ c: Int) -> Bool {
        var d1 = Array(repeating: 0, count: 26)
        var d2 = Array(repeating: 0, count: 10)
        for a in 0..<r {
            let row = Array(pattern[a])
            for b in 0..<c {
                let x = i + a, y = j + b
                let ch = row[b]
                if ch >= "0" && ch <= "9" {
                    if Int(String(ch))! != board[x][y] { return false }
                } else {
                    let v = Int(ch.asciiValue! - Character("a").asciiValue!)
                    if d1[v] > 0 && d1[v] - 1 != board[x][y] { return false }
                    if d2[board[x][y]] > 0 && d2[board[x][y]] - 1 != v { return false }
                    d1[v] = board[x][y] + 1
                    d2[board[x][y]] = v + 1
                }
            }
        }
        return true
    }
}
