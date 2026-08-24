// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

class Solution {
    func minXor(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var g = Array(repeating: 0, count: n + 1)
        for i in 1...n { g[i] = g[i - 1] ^ nums[i - 1] }
        let Inf = Int.max / 2
        var f = Array(repeating: Array(repeating: Inf, count: k + 1), count: n + 1)
        f[0][0] = 0
        for i in 1...n {
            for j in 1...min(i, k) {
                for h in (j - 1)..<i {
                    f[i][j] = min(f[i][j], max(f[h][j - 1], g[i] ^ g[h]))
                }
            }
        }
        return f[n][k]
    }
}
