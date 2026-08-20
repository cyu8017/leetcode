// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

class Solution {
    func palindromePartition(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var cost = [[Int]](repeating: [Int](repeating: 0, count: n), count: n)
        for length in 2...n {
            for i in 0...(n - length) {
                let j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (chars[i] == chars[j] ? 0 : 1)
            }
        }
        var dp = [[Int]](repeating: [Int](repeating: Int.max / 4, count: k + 1), count: n + 1)
        dp[0][0] = 0
        for i in 1...n {
            for parts in 1...min(k, i) {
                for j in 0..<i {
                    dp[i][parts] = min(dp[i][parts], dp[j][parts - 1] + cost[j][i - 1])
                }
            }
        }
        return dp[n][k]
    }
}
