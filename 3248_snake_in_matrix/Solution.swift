// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

class Solution {
    func finalPositionOfSnake(_ n: Int, _ commands: [String]) -> Int {
        var x = 0, y = 0
        for c in commands {
            switch c.first! {
            case "U": x -= 1
            case "D": x += 1
            case "L": y -= 1
            default: y += 1
            }
        }
        return x * n + y
    }
}
