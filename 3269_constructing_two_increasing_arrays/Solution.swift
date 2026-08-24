// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

class Solution {
    func minLargest(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count, m = nums2.count
        let inf = 1_000_000_000
        var dp = Array(repeating: Array(repeating: inf, count: m + 1), count: n + 1)
        dp[0][0] = 0
        for i in 0...n {
            for j in 0...m {
                if dp[i][j] == inf { continue }
                let prev = dp[i][j]
                if i < n {
                    var need = prev + 1
                    if nums1[i] == 0 {
                        if need % 2 != 0 { need += 1 }
                    } else {
                        if need % 2 == 0 { need += 1 }
                    }
                    dp[i + 1][j] = min(dp[i + 1][j], need)
                }
                if j < m {
                    var need = prev + 1
                    if nums2[j] == 0 {
                        if need % 2 != 0 { need += 1 }
                    } else {
                        if need % 2 == 0 { need += 1 }
                    }
                    dp[i][j + 1] = min(dp[i][j + 1], need)
                }
            }
        }
        return dp[n][m]
    }
}
