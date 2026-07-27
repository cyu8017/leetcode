// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

class Solution {
    func maxHeight(_ cuboids: [[Int]]) -> Int {
        var a = cuboids.map { $0.sorted() }
        a.sort {
            for d in 0..<3 {
                if $0[d] != $1[d] { return $0[d] < $1[d] }
            }
            return false
        }
        let n = a.count
        var dp = Array(repeating: 0, count: n)
        for i in 0..<n {
            dp[i] = a[i][2]
            for j in 0..<i {
                if (0..<3).allSatisfy({ a[j][$0] <= a[i][$0] }) {
                    dp[i] = max(dp[i], dp[j] + a[i][2])
                }
            }
        }
        return dp.max() ?? 0
    }
}
