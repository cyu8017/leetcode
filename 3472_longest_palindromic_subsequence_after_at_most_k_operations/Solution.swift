// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

class Solution {
    func longestPalindromicSubsequence(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var dp = Array(repeating: Array(repeating: Array(repeating: -1, count: k + 1), count: n), count: n)
        func distCirc(_ a: Character, _ b: Character) -> Int {
            let d = abs(Int(a.asciiValue!) - Int(b.asciiValue!))
            return min(d, 26 - d)
        }
        func dfs(_ i: Int, _ j: Int, _ ops: Int) -> Int {
            if i > j { return 0 }
            if i == j { return 1 }
            if dp[i][j][ops] != -1 { return dp[i][j][ops] }
            var best = max(dfs(i + 1, j, ops), dfs(i, j - 1, ops))
            let cost = distCirc(chars[i], chars[j])
            if cost <= ops { best = max(best, 2 + dfs(i + 1, j - 1, ops - cost)) }
            dp[i][j][ops] = best
            return best
        }
        return dfs(0, n - 1, k)
    }
}
