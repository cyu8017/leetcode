// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution {
    func minimumBeautifulSubstrings(_ s: String) -> Int {
        let n = s.count
        var pow5 = Set<String>()
        var x = 1
        while true {
            let b = String(x, radix: 2)
            if b.count > n { break }
            pow5.insert(b)
            x *= 5
        }
        let INF = 1 << 30
        var dp = Array(repeating: INF, count: n + 1)
        dp[0] = 0
        let chars = Array(s)
        for i in 0..<n {
            if dp[i] == INF || chars[i] == "0" { continue }
            for j in (i + 1)...n {
                if pow5.contains(String(chars[i..<j])) {
                    dp[j] = min(dp[j], dp[i] + 1)
                }
            }
        }
        return dp[n] == INF ? -1 : dp[n]
    }
}
