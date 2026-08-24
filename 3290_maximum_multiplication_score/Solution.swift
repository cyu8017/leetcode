// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

class Solution {
    func maxScore(_ a: [Int], _ b: [Int]) -> Int {
        let neg = -(1 << 62)
        var dp = [0, neg, neg, neg, neg]
        for x in b {
            for k in stride(from: 4, through: 1, by: -1) {
                if dp[k - 1] == neg { continue }
                let v = dp[k - 1] + a[k - 1] * x
                if v > dp[k] { dp[k] = v }
            }
        }
        return dp[4]
    }
}
