// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

class Solution {
    func splitArray(_ nums: [Int]) -> Int {
        let n = nums.count
        var s = Array(repeating: 0, count: n)
        var f = Array(repeating: true, count: n)
        var g = Array(repeating: true, count: n)
        s[0] = nums[0]
        if n > 1 {
            for i in 1..<n {
                s[i] = s[i - 1] + nums[i]
                f[i] = f[i - 1]
                if nums[i] <= nums[i - 1] { f[i] = false }
            }
            for i in stride(from: n - 2, through: 0, by: -1) {
                g[i] = g[i + 1]
                if nums[i] <= nums[i + 1] { g[i] = false }
            }
        }
        let inf = Int.max / 4
        var ans = inf
        for i in 0..<(n - 1) {
            if f[i] && g[i + 1] {
                let s1 = s[i], s2 = s[n - 1] - s[i]
                ans = min(ans, abs(s1 - s2))
            }
        }
        return ans < inf ? ans : -1
    }
}
