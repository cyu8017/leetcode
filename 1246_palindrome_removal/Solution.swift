// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

class Solution {
    func minimumMoves(_ arr: [Int]) -> Int {
        let n = arr.count
        var dp = [[Int]](repeating: [Int](repeating: 0, count: n), count: n)
        for i in 0..<n { dp[i][i] = 1 }
        for len in 2...n {
            for i in 0...(n - len) {
                let j = i + len - 1
                dp[i][j] = dp[i + 1][j] + 1
                if arr[i] == arr[i + 1] { dp[i][j] = min(dp[i][j], (i + 2 <= j ? dp[i + 2][j] : 0) + 1) }
                for k in (i + 2)...j where arr[i] == arr[k] {
                    dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + (k + 1 <= j ? dp[k + 1][j] : 0))
                }
            }
        }
        return dp[0][n - 1]
    }
}
