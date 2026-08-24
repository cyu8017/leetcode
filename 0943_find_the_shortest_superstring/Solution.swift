// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

class Solution {
    func shortestSuperstring(_ words: [String]) -> String {
        let n = words.count
        var overlap = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n where i != j {
                let a = words[i], b = words[j]
                for k in stride(from: min(a.count, b.count), through: 1, by: -1) {
                    if a.suffix(k) == b.prefix(k) {
                        overlap[i][j] = k
                        break
                    }
                }
            }
        }
        let N = 1 << n
        var dp = Array(repeating: Array(repeating: nil as String?, count: n), count: N)
        for i in 0..<n { dp[1 << i][i] = words[i] }
        for mask in 0..<N {
            for last in 0..<n {
                guard (mask & (1 << last)) != 0, let cur = dp[mask][last] else { continue }
                for nxt in 0..<n where (mask & (1 << nxt)) == 0 {
                    let ov = overlap[last][nxt]
                    let cand = cur + String(words[nxt].dropFirst(ov))
                    let nmask = mask | (1 << nxt)
                    if dp[nmask][nxt] == nil || cand.count < dp[nmask][nxt]!.count {
                        dp[nmask][nxt] = cand
                    }
                }
            }
        }
        let full = N - 1
        var best: String?
        for i in 0..<n {
            if let s = dp[full][i], best == nil || s.count < best!.count { best = s }
        }
        return best ?? ""
    }
}
