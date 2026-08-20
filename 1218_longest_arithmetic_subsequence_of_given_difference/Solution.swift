// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution {
    func longestSubsequence(_ arr: [Int], _ difference: Int) -> Int {
        var dp: [Int: Int] = [:]
        var ans = 0
        for x in arr {
            let len = (dp[x - difference] ?? 0) + 1
            dp[x] = len
            ans = max(ans, len)
        }
        return ans
    }
}
