// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

class Solution {
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ K: Int) -> Int {
        let n = nums1.count, m = nums2.count
        let NEG = Int.min / 4
        var f = Array(repeating: Array(repeating: [Int](repeating: NEG, count: K + 1), count: m + 1), count: n + 1)
        f[0][0][0] = 0
        for i in 0...n {
            for j in 0...m {
                for k in 0...K {
                    if i > 0 { f[i][j][k] = max(f[i][j][k], f[i - 1][j][k]) }
                    if j > 0 { f[i][j][k] = max(f[i][j][k], f[i][j - 1][k]) }
                    if i > 0 && j > 0 && k > 0 {
                        f[i][j][k] = max(f[i][j][k], f[i - 1][j - 1][k - 1] + nums1[i - 1] * nums2[j - 1])
                    }
                }
            }
        }
        return f[n][m][K]
    }
}
