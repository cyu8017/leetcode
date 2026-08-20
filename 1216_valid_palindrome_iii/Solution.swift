// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

class Solution {
    func isValidPalindrome(_ s: String, _ k: Int) -> Bool {
        let chars = Array(s)
        let n = chars.count
        var dp = [Int](repeating: 0, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            var prev = 0
            for j in (i + 1)..<n {
                let tmp = dp[j]
                if chars[i] == chars[j] {
                    dp[j] = prev
                } else {
                    dp[j] = 1 + min(dp[j], dp[j - 1])
                }
                prev = tmp
            }
        }
        return dp[n - 1] <= k
    }
}
