// LeetCode 0097 - Interleaving String
// https://leetcode.com/problems/interleaving-string/

class Solution {
    func isInterleave(_ s1: String, _ s2: String, _ s3: String) -> Bool {
        if s1.count + s2.count != s3.count {
            return false
        }

        let a = Array(s1)
        let b = Array(s2)
        let c = Array(s3)
        let m = a.count
        let n = b.count
        var dp = Array(repeating: false, count: n + 1)
        dp[0] = true

        if n > 0 {
            for j in 1...n {
                dp[j] = dp[j - 1] && b[j - 1] == c[j - 1]
            }
        }

        if m == 0 {
            return dp[n]
        }

        for i in 1...m {
            dp[0] = dp[0] && a[i - 1] == c[i - 1]
            if n > 0 {
                for j in 1...n {
                    dp[j] = (dp[j] && a[i - 1] == c[i + j - 1]) ||
                        (dp[j - 1] && b[j - 1] == c[i + j - 1])
                }
            }
        }

        return dp[n]
    }
}
