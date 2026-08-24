// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

class Solution {
    func minOperations(_ s1: String, _ s2: String, _ x: Int) -> Int {
        let a = Array(s1), b = Array(s2)
        var diff: [Int] = []
        for i in 0..<a.count where a[i] != b[i] {
            diff.append(i)
        }
        let m = diff.count
        if m % 2 == 1 { return -1 }
        if m == 0 { return 0 }
        var dp = Array(repeating: 0.0, count: m + 1)
        for i in 1...m {
            dp[i] = dp[i - 1] + Double(x) / 2.0
            if i >= 2 {
                dp[i] = min(dp[i], dp[i - 2] + Double(diff[i - 1] - diff[i - 2]))
            }
        }
        return Int(dp[m])
    }
}
