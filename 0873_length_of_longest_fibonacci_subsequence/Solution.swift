// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution {
    func lenLongestFibSubseq(_ arr: [Int]) -> Int {
        let n = arr.count
        var index = [Int: Int]()
        for i in 0..<n { index[arr[i]] = i }
        var dp = Array(repeating: Array(repeating: 2, count: n), count: n)
        var ans = 0
        for j in 0..<n {
            for i in 0..<j {
                if let k = index[arr[j] - arr[i]], k < i {
                    dp[i][j] = dp[k][i] + 1
                    ans = max(ans, dp[i][j])
                }
            }
        }
        return ans >= 3 ? ans : 0
    }
}
