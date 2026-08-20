// LeetCode 1958 - Check if Move is Legal
// https://leetcode.com/problems/check-if-move-is-legal/

class Solution {
    func checkMove(_ board: [[Character]], _ rMove: Int, _ cMove: Int, _ color: Character) -> Bool {
        let opp: Character = color == "B" ? "W" : "B"
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for (dr, dc) in dirs {
            var r = rMove + dr, c = cMove + dc, steps = 0
            while r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] == opp {
                r += dr; c += dc; steps += 1
            }
            if steps > 0 && r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] == color {
                return true
            }
        }
        return false
    }
}
