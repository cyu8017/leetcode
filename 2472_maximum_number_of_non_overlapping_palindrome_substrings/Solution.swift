// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution {
    func maxPalindromes(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var isPal = [[Bool]](repeating: [Bool](repeating: false, count: n), count: n)
        for i in 0..<n { isPal[i][i] = true }
        if n >= 2 {
            for i in 0..<(n - 1) { isPal[i][i + 1] = chars[i] == chars[i + 1] }
        }
        if n >= 3 {
            for length in 3...n {
                for i in 0...(n - length) {
                    let j = i + length - 1
                    isPal[i][j] = chars[i] == chars[j] && isPal[i + 1][j - 1]
                }
            }
        }
        var dp = [Int](repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            dp[i] = dp[i + 1]
            if i + k - 1 < n {
                for j in (i + k - 1)..<n {
                    if isPal[i][j] { dp[i] = max(dp[i], 1 + dp[j + 1]) }
                }
            }
        }
        return dp[0]
    }
}
