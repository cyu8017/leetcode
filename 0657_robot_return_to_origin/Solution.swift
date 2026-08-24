// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/

class Solution {
    func judgeCircle(_ moves: String) -> Bool {
        var x = 0, y = 0
        for move in moves {
            if move == "U" { y += 1 }
            else if move == "D" { y -= 1 }
            else if move == "L" { x -= 1 }
            else if move == "R" { x += 1 }
        }
        return x == 0 && y == 0
    }
}
