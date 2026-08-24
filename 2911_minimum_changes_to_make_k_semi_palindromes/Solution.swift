// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

class Solution {
    private var chars: [Character] = []

    func minimumChanges(_ s: String, _ k: Int) -> Int {
        chars = Array(s)
        let n = chars.count
        var cost = Array(repeating: Array(repeating: 1 << 20, count: n), count: n)
        for i in 0..<n {
            for j in (i + 1)..<n {
                cost[i][j] = semiCost(i, j)
            }
        }
        var dp = Array(repeating: Array(repeating: 1 << 20, count: n + 1), count: k + 1)
        dp[0][0] = 0
        for p in 1...k {
            for i in 1...n {
                if i >= 2 {
                    for t in 0..<(i - 1) {
                        dp[p][i] = min(dp[p][i], dp[p - 1][t] + cost[t][i - 1])
                    }
                }
            }
        }
        return dp[k][n]
    }

    private func semiCost(_ l: Int, _ r: Int) -> Int {
        let length = r - l + 1
        var best = 1 << 20
        for d in 1..<length where length % d == 0 {
            var chg = 0
            for start in 0..<d {
                var seq: [Character] = []
                var i = l + start
                while i <= r {
                    seq.append(chars[i])
                    i += d
                }
                var a = 0, b = seq.count - 1
                while a < b {
                    if seq[a] != seq[b] { chg += 1 }
                    a += 1
                    b -= 1
                }
            }
            best = min(best, chg)
        }
        return best
    }
}
