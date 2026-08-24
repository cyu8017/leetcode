// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

class Solution {
    func countSubMultisets(_ nums: [Int], _ l: Int, _ r0: Int) -> Int {
        let mod = 1_000_000_007
        var freq: [Int: Int] = [:]
        var total = 0
        for v in nums {
            freq[v, default: 0] += 1
            total += v
        }
        if total < l { return 0 }
        var r = min(r0, total)
        var dp = Array(repeating: 0, count: r + 1)
        dp[0] = 1
        let zeros = freq[0, default: 0]
        freq.removeValue(forKey: 0)
        for (v, c) in freq {
            var ndp = Array(repeating: 0, count: r + 1)
            for sum in 0...r where dp[sum] != 0 {
                var k = 0
                while k <= c && sum + k * v <= r {
                    ndp[sum + k * v] = (ndp[sum + k * v] + dp[sum]) % mod
                    k += 1
                }
            }
            dp = ndp
        }
        var ans = 0
        for s in l...r { ans = (ans + dp[s]) % mod }
        return ans * (zeros + 1) % mod
    }
}
