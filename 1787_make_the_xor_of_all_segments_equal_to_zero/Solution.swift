// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

class Solution {
    func minChanges(_ nums: [Int], _ k: Int) -> Int {
        var freq = Array(repeating: [Int](repeating: 0, count: 1024), count: k)
        var size = [Int](repeating: 0, count: k)
        for (i, x) in nums.enumerated() {
            freq[i % k][x] += 1
            size[i % k] += 1
        }
        let inf = 1_000_000_000
        var dp = [Int](repeating: inf, count: 256)
        dp[0] = 0
        for i in 0..<k {
            var ndp = [Int](repeating: inf, count: 256)
            for xv in 0..<256 {
                let cost = size[i] - freq[i][xv]
                for xo in 0..<256 {
                    if dp[xo] == inf {
                        continue
                    }
                    let key = xo ^ xv
                    if dp[xo] + cost < ndp[key] {
                        ndp[key] = dp[xo] + cost
                    }
                }
            }
            dp = ndp
        }
        return dp[0]
    }
}
