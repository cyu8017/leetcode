// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/


class Solution {
    func countWays(_ word1: String, _ word2: String, _ target: String) -> Int {
        let mod = 1_000_000_007
        let w1 = Array(word1), w2 = Array(word2), t = Array(target)
        let n1 = w1.count, n2 = w2.count
        func idx(_ i: Int, _ j: Int, _ mask: Int) -> Int {
            ((i * (n2 + 1) + j) * 4) + mask
        }
        let size = (n1 + 1) * (n2 + 1) * 4
        var dp = Array(repeating: 0, count: size)
        var next = Array(repeating: 0, count: size)
        dp[idx(0, 0, 0)] = 1
        for ti in 0..<t.count {
            let ch = t[ti]
            next = Array(repeating: 0, count: size)
            for j in 0...n2 {
                var prefix = Array(repeating: 0, count: 4)
                for a in 0..<n1 {
                    for mask in 0..<4 {
                        prefix[mask] += dp[idx(a, j, mask)]
                        if prefix[mask] >= mod { prefix[mask] -= mod }
                    }
                    if w1[a] == ch {
                        for mask in 0..<4 {
                            let at = idx(a + 1, j, mask | 1)
                            next[at] += prefix[mask]
                            if next[at] >= mod { next[at] -= mod }
                        }
                    }
                }
            }
            for i in 0...n1 {
                var prefix = Array(repeating: 0, count: 4)
                for b in 0..<n2 {
                    for mask in 0..<4 {
                        prefix[mask] += dp[idx(i, b, mask)]
                        if prefix[mask] >= mod { prefix[mask] -= mod }
                    }
                    if w2[b] == ch {
                        for mask in 0..<4 {
                            let at = idx(i, b + 1, mask | 2)
                            next[at] += prefix[mask]
                            if next[at] >= mod { next[at] -= mod }
                        }
                    }
                }
            }
            swap(&dp, &next)
        }
        var answer = 0
        for i in 0...n1 {
            for j in 0...n2 {
                answer += dp[idx(i, j, 3)]
                if answer >= mod { answer -= mod }
            }
        }
        return answer
    }
}
