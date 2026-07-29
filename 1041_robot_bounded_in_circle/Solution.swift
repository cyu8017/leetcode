// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

class Solution {
    func isRobotBounded(_ instructions: String) -> Bool {
        var x = 0, y = 0
        var dx = 0, dy = 1
        for ch in instructions {
            if ch == "G" {
                x += dx; y += dy
            } else if ch == "L" {
                let ndx = -dy
                dy = dx
                dx = ndx
            } else {
                let ndx = dy
                dy = -dx
                dx = ndx
            }
        }
        return (x == 0 && y == 0) || !(dx == 0 && dy == 1)
    }
}
