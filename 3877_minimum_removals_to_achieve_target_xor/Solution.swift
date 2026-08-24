// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

class Solution {
    func minRemovals(_ nums: [Int], _ target: Int) -> Int {
        var mx = 0
        for x in nums { mx = max(mx, x) }
        var m = 0
        if mx > 0 {
            var u = mx
            while u != 0 { m += 1; u >>= 1 }
        }
        if (1 << m) <= target { return -1 }
        let n = nums.count
        let N = 1 << m
        var f = Array(repeating: [Int](repeating: Int.min, count: N), count: n + 1)
        f[0][0] = 0
        for i in 1...n {
            let x = nums[i - 1]
            for j in 0..<N {
                f[i][j] = f[i - 1][j]
                if f[i - 1][j ^ x] != Int.min {
                    f[i][j] = max(f[i][j], f[i - 1][j ^ x] + 1)
                }
            }
        }
        if f[n][target] < 0 { return -1 }
        return n - f[n][target]
    }
}
