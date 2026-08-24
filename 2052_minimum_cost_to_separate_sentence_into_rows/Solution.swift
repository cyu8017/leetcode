// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

class Solution {
    func minimumCost(_ sentence: String, _ k: Int) -> Int {
        let words = sentence.split(separator: " ").map(String.init)
        let n = words.count
        var dp = [Int](repeating: Int.max / 4, count: n + 1)
        dp[n] = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            var length = -1
            for j in i..<n {
                length += 1 + words[j].count
                if length > k { break }
                var cost = 0
                if j < n - 1 {
                    let extra = k - length
                    cost = extra * extra
                }
                dp[i] = min(dp[i], cost + dp[j + 1])
            }
        }
        return dp[0]
    }
}
