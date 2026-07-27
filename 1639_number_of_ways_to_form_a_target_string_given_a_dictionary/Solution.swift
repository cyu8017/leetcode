// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution {
    func numWays(_ words: [String], _ target: String) -> Int {
        let MOD = 1_000_000_007
        let m = words[0].count
        let t = Array(target)
        var dp = [Int](repeating: 0, count: t.count + 1)
        dp[0] = 1
        let wordChars = words.map { Array($0) }
        for j in 0..<m {
            var count = [Int](repeating: 0, count: 26)
            for w in wordChars {
                count[Int(w[j].asciiValue! - 97)] += 1
            }
            var i = min(j + 1, t.count)
            while i > 0 {
                let add = Int((Int64(dp[i - 1]) * Int64(count[Int(t[i - 1].asciiValue! - 97)])) % Int64(MOD))
                dp[i] = (dp[i] + add) % MOD
                i -= 1
            }
        }
        return dp[t.count]
    }
}
