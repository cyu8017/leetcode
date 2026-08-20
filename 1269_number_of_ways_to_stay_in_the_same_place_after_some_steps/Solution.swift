// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution {
    func numWays(_ steps: Int, _ arrLen: Int) -> Int {
        let MOD = 1_000_000_007
        let maxPos = min(arrLen - 1, steps)
        var dp = [Int](repeating: 0, count: maxPos + 1)
        dp[0] = 1
        for _ in 0..<steps {
            var next = [Int](repeating: 0, count: maxPos + 1)
            for i in 0...maxPos {
                next[i] = dp[i]
                if i > 0 { next[i] = (next[i] + dp[i - 1]) % MOD }
                if i < maxPos { next[i] = (next[i] + dp[i + 1]) % MOD }
            }
            dp = next
        }
        return dp[0]
    }
}
