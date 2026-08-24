// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

class Solution {
    func goodBinaryStrings(_ minLength: Int, _ maxLength: Int, _ oneGroup: Int, _ zeroGroup: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = [Int](repeating: 0, count: maxLength + 1)
        dp[0] = 1
        for i in 0...maxLength {
            if dp[i] == 0 { continue }
            if i + oneGroup <= maxLength { dp[i + oneGroup] = (dp[i + oneGroup] + dp[i]) % MOD }
            if i + zeroGroup <= maxLength { dp[i + zeroGroup] = (dp[i + zeroGroup] + dp[i]) % MOD }
        }
        var ans = 0
        for i in minLength...maxLength { ans = (ans + dp[i]) % MOD }
        return ans
    }
}
