// LeetCode 1406 - Stone Game III
// https://leetcode.com/problems/stone-game-iii/

class Solution {
    func stoneGameIII(_ stoneValue: [Int]) -> String {
        let n = stoneValue.count
        var dp = Array(repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            var take = 0
            dp[i] = Int.min / 4
            for j in i..<min(i + 3, n) {
                take += stoneValue[j]
                dp[i] = max(dp[i], take - dp[j + 1])
            }
        }
        if dp[0] > 0 { return "Alice" }
        if dp[0] < 0 { return "Bob" }
        return "Tie"
    }
}
