// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

class Solution {
    func numRookCaptures(_ board: [[Character]]) -> Int {
        let m = board.count, n = board[0].count
        var r = -1, c = -1
        for i in 0..<m {
            for j in 0..<n where board[i][j] == "R" {
                r = i; c = j
            }
        }
        if r < 0 { return 0 }
        var ans = 0
        for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
            var i = r + dr, j = c + dc
            while i >= 0 && i < m && j >= 0 && j < n {
                if board[i][j] == "B" { break }
                if board[i][j] == "p" { ans += 1; break }
                i += dr; j += dc
            }
        }
        return ans
    }
}
