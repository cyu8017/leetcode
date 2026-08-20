// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

class Solution {
    func maxSizeSlices(_ slices: [Int]) -> Int {
        let k = slices.count / 3
        func line(_ a: [Int]) -> Int {
            var dp = Array(repeating: Array(repeating: 0, count: k + 1), count: a.count + 2)
            for (idx, x) in a.enumerated() {
                let i = idx + 2
                for j in 1...k {
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + x)
                }
            }
            return dp[a.count + 1][k]
        }
        return max(line(Array(slices.dropLast())), line(Array(slices.dropFirst())))
    }
}
