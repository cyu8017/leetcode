// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

class Solution {
    func minimumCost(_ target: String, _ words: [String], _ costs: [Int]) -> Int {
        let inf = Int.max / 4
        let n = target.count
        var dp = Array(repeating: inf, count: n + 1)
        dp[0] = 0
        var best: [String: Int] = [:]
        for i in 0..<words.count {
            if best[words[i]] == nil || costs[i] < best[words[i]]! { best[words[i]] = costs[i] }
        }
        let t = target
        for i in 0..<n {
            if dp[i] == inf { continue }
            for (w, c) in best {
                let L = w.count
                if i + L <= n {
                    let start = t.index(t.startIndex, offsetBy: i)
                    if t[start...].hasPrefix(w) && dp[i] + c < dp[i + L] {
                        dp[i + L] = dp[i] + c
                    }
                }
            }
        }
        return dp[n] == inf ? -1 : dp[n]
    }
}
