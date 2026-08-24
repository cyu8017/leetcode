// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

class Solution {
    func maxSum(_ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        var cnt = Array(repeating: 0, count: 32)
        for v in nums {
            for b in 0..<32 where (v & (1 << b)) != 0 {
                cnt[b] += 1
            }
        }
        var ans = 0
        for _ in 0..<k {
            var cur = 0
            for b in 0..<32 where cnt[b] > 0 {
                cur |= 1 << b
                cnt[b] -= 1
            }
            let c = cur % mod
            ans = (ans + c * c % mod) % mod
        }
        return ans
    }
}
