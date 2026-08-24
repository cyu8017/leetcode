// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

class Solution {
    func maxWeight(_ weights: [Int], _ w1: Int, _ w2: Int) -> Int {
        var f = Array(repeating: Array(repeating: 0, count: w2 + 1), count: w1 + 1)
        for x in weights {
            for j in stride(from: w1, through: 0, by: -1) {
                for k in stride(from: w2, through: 0, by: -1) {
                    if x <= j { f[j][k] = max(f[j][k], f[j - x][k] + x) }
                    if x <= k { f[j][k] = max(f[j][k], f[j][k - x] + x) }
                }
            }
        }
        return f[w1][w2]
    }
}
