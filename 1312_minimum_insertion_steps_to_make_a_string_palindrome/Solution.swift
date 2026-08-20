// LeetCode 1312 - Minimum Insertion Steps to Make a String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution {
    func minInsertions(_ s: String) -> Int {
        let chars = Array(s), n = chars.count
        var dp = Array(repeating: 0, count: n)
        for left in stride(from: n - 2, through: 0, by: -1) {
            var diagonal = 0
            for right in (left + 1)..<n {
                let old = dp[right]
                if chars[left] == chars[right] { dp[right] = diagonal }
                else { dp[right] = 1 + min(dp[right], dp[right - 1]) }
                diagonal = old
            }
        }
        return n == 0 ? 0 : dp[n - 1]
    }
}
