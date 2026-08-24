// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

class Solution {
    func minExtraChar(_ s: String, _ dictionary: [String]) -> Int {
        let dict = Set(dictionary)
        let n = s.count
        let chars = Array(s)
        var dp = Array(repeating: n, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            for j in (i + 1)...n {
                let sub = String(chars[i..<j])
                if dict.contains(sub) { dp[j] = min(dp[j], dp[i]) }
            }
        }
        return dp[n]
    }
}
