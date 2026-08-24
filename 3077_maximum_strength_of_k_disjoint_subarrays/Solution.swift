// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

class Solution {
    func maximumStrength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let INF = Int.min / 4
        var f = Array(repeating: Array(repeating: [INF, INF], count: k + 1), count: n + 1)
        f[0][0][0] = 0
        for i in 1...n {
            let x = nums[i - 1]
            for j in 0...k {
                let sign = (j & 1) != 0 ? 1 : -1
                let val = sign * x * (k - j + 1)
                f[i][j][0] = max(f[i - 1][j][0], f[i - 1][j][1])
                f[i][j][1] = max(f[i][j][1], f[i - 1][j][1] + val)
                if j > 0 {
                    let t = max(f[i - 1][j - 1][0], f[i - 1][j - 1][1]) + val
                    f[i][j][1] = max(f[i][j][1], t)
                }
            }
        }
        return max(f[n][k][0], f[n][k][1])
    }
}
