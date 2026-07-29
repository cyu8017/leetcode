// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

class Solution {
    func longestStrChain(_ words: [String]) -> Int {
        let words = words.sorted { $0.count < $1.count }
        var dp = [String: Int]()
        var ans = 1
        for w in words {
            var best = 1
            let arr = Array(w)
            for i in 0..<arr.count {
                let prev = String(arr[0..<i] + arr[(i + 1)...])
                if let len = dp[prev] {
                    best = max(best, len + 1)
                }
            }
            dp[w] = best
            ans = max(ans, best)
        }
        return ans
    }
}
