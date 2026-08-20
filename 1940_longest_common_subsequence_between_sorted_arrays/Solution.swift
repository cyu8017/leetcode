// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

class Solution {
    func longestCommonSubsequence(_ arrays: [[Int]]) -> [Int] {
        var cnt: [Int: Int] = [:]
        for arr in arrays {
            for x in arr { cnt[x, default: 0] += 1 }
        }
        let m = arrays.count
        return arrays[0].filter { cnt[$0] == m }
    }
}
