// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

class Solution {
    func superEggDrop(_ k: Int, _ n: Int) -> Int {
        var dp = Array(repeating: 0, count: k + 1)
        var moves = 0
        while dp[k] < n {
            moves += 1
            for eggs in stride(from: k, through: 1, by: -1) {
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
            }
        }
        return moves
    }
}
