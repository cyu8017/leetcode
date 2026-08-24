// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

class Solution {
    func maxA(_ n: Int) -> Int {
        var dp = Array(0...n)
        for i in 1...n {
            if i >= 3 {
                for j in 0..<(i - 2) {
                    dp[i] = max(dp[i], dp[j] * (i - j - 1))
                }
            }
        }
        return dp[n]
    }
}
