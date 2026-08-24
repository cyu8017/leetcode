// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

class Solution {
    func countTexts(_ pressedKeys: String) -> Int {
        let mod = 1_000_000_007
        let s = Array(pressedKeys)
        let n = s.count
        var dp = [Int](repeating: 0, count: n + 1)
        dp[0] = 1
        for i in 1...n {
            dp[i] = dp[i - 1]
            let maxPress = (s[i - 1] == "7" || s[i - 1] == "9") ? 4 : 3
            var j = 2
            while j <= maxPress && j <= i {
                if s[i - j] != s[i - 1] { break }
                dp[i] = (dp[i] + dp[i - j]) % mod
                j += 1
            }
        }
        return dp[n]
    }
}
