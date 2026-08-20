// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

class Solution {
    func alphabetBoardPath(_ target: String) -> String {
        var row = 0, col = 0
        var ans = ""
        for ch in target {
            let idx = Int(ch.asciiValue! - Character("a").asciiValue!)
            let r = idx / 5, c = idx % 5
            if r < row {
                ans += String(repeating: "U", count: row - r)
                row = r
            }
            if c < col {
                ans += String(repeating: "L", count: col - c)
                col = c
            }
            if c > col {
                ans += String(repeating: "R", count: c - col)
                col = c
            }
            if r > row {
                ans += String(repeating: "D", count: r - row)
                row = r
            }
            ans += "!"
        }
        return ans
    }
}
