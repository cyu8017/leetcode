// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

class Solution {
    func countPartitions(_ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        var sl = [Int: Int]()
        let n = nums.count
        var f = Array(repeating: 0, count: n + 1)
        var g = Array(repeating: 0, count: n + 1)
        f[0] = 1; g[0] = 1
        var l = 1
        for r in 1...n {
            sl[nums[r - 1], default: 0] += 1
            while sl.keys.max()! - sl.keys.min()! > k {
                let v = nums[l - 1]
                let c = sl[v]!
                if c == 1 { sl[v] = nil } else { sl[v] = c - 1 }
                l += 1
            }
            f[r] = g[r - 1]
            if l >= 2 { f[r] = (f[r] - g[l - 2] + mod) % mod }
            g[r] = (g[r - 1] + f[r]) % mod
        }
        return f[n]
    }
}
