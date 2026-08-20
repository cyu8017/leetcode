// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution {
    func numRollsToTarget(_ n: Int, _ k: Int, _ target: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = [Int](repeating: 0, count: target + 1)
        dp[0] = 1
        for _ in 0..<n {
            var neu = [Int](repeating: 0, count: target + 1)
            for s in 0...target where dp[s] != 0 {
                for face in 1...k where s + face <= target {
                    neu[s + face] = (neu[s + face] + dp[s]) % MOD
                }
            }
            dp = neu
        }
        return dp[target]
    }
}
