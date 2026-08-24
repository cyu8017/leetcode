// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/


class Solution {
    func minCost(_ source: String, _ target: String, _ rules: [[String]], _ costs: [Int]) -> Int {
        let src = Array(source), tgt = Array(target)
        let n = src.count
        if tgt.count != n { return -1 }
        var dp = Array(repeating: Int.max, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            if dp[i] == Int.max { continue }
            if src[i] == tgt[i] && dp[i] < dp[i + 1] { dp[i + 1] = dp[i] }
            for j in 0..<rules.count {
                let p = Array(rules[j][0])
                let r = Array(rules[j][1])
                let plen = p.count
                if i + plen > n { continue }
                var c = costs[j]
                var ok = true
                for k in 0..<plen {
                    if r[k] != tgt[i + k] { ok = false; break }
                    if p[k] == "*" { c += 1 }
                    else if p[k] != src[i + k] { ok = false; break }
                }
                if ok && dp[i] <= Int.max - c && dp[i] + c < dp[i + plen] {
                    dp[i + plen] = dp[i] + c
                }
            }
        }
        return dp[n] == Int.max ? -1 : dp[n]
    }
}
