// LeetCode 0174 - Dungeon Game
// https://leetcode.com/problems/dungeon-game/

class Solution {
    func calculateMinimumHP(_ dungeon: [[Int]]) -> Int {
        let rows = dungeon.count
        let cols = dungeon[0].count
        let infinity = Int.max / 2
        var dp = Array(repeating: Array(repeating: infinity, count: cols + 1), count: rows + 1)
        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1

        for row in stride(from: rows - 1, through: 0, by: -1) {
            for col in stride(from: cols - 1, through: 0, by: -1) {
                dp[row][col] = max(1, min(dp[row + 1][col], dp[row][col + 1]) - dungeon[row][col])
            }
        }
        return dp[0][0]
    }
}