// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

class Solution {
    func winnerSquareGame(_ n: Int) -> Bool {
        var win = Array(repeating: false, count: n + 1)
        for value in 1...n {
            var root = 1
            while root * root <= value {
                if !win[value - root * root] {
                    win[value] = true
                    break
                }
                root += 1
            }
        }
        return win[n]
    }
}
