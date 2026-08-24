// LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

class Solution {
    func longestArithmetic(_ nums: [Int]) -> Int {
        let n = nums.count
        var d = [Int](repeating: 0, count: n)
        if n > 1 {
            for i in 1..<n { d[i] = nums[i] - nums[i - 1] }
        }
        var f = [Int](repeating: 2, count: n)
        var g = [Int](repeating: 2, count: n)
        f[0] = 1
        g[n - 1] = 1
        if n > 2 {
            for i in 2..<n {
                if d[i] == d[i - 1] { f[i] = f[i - 1] + 1 }
            }
            for i in stride(from: n - 3, through: 0, by: -1) {
                if d[i + 1] == d[i + 2] { g[i] = g[i + 1] + 1 }
            }
        }
        var ans = 3
        for i in 0..<n {
            ans = max(ans, max(f[i], g[i]))
            if i > 0 { ans = max(ans, f[i - 1] + 1) }
            if i + 1 < n { ans = max(ans, g[i + 1] + 1) }
            if i > 0 && i < n - 1 {
                var diff = nums[i + 1] - nums[i - 1]
                if diff % 2 == 0 {
                    diff /= 2
                    var k = 3
                    if i > 1 && diff == d[i - 1] { k += f[i - 1] - 1 }
                    if i < n - 2 && diff == d[i + 2] { k += g[i + 1] - 1 }
                    ans = max(ans, k)
                }
            }
        }
        return ans
    }
}
