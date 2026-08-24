// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/


class Solution {
    func minOperations(_ s1: String, _ s2: String) -> Int {
        let a = Array(s1), b = Array(s2)
        let infinity = 1_000_000_000
        var dp = [0, infinity]
        let n = a.count
        for i in 0..<n {
            var next = [infinity, infinity]
            for forcedZero in 0...1 {
                if dp[forcedZero] == infinity { continue }
                var current = a[i]
                if forcedZero == 1 { current = "0" }
                var direct = dp[forcedZero]
                if current == "0" && b[i] == "1" { direct += 1 }
                else if current == "1" && b[i] == "0" { direct = infinity }
                next[0] = min(next[0], direct)
                if i + 1 < n {
                    var cost = dp[forcedZero] + 1
                    if current == "0" { cost += 1 }
                    if a[i + 1] == "0" { cost += 1 }
                    if b[i] == "1" { cost += 1 }
                    next[1] = min(next[1], cost)
                }
            }
            dp = next
        }
        return dp[0] == infinity ? -1 : dp[0]
    }
}
