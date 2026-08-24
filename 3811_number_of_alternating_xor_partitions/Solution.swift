// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

class Solution {
    func alternatingXOR(_ nums: [Int], _ target1: Int, _ target2: Int) -> Int {
        let MOD = 1_000_000_007
        var cnt1 = [Int: Int]()
        var cnt2 = [0: 1]
        var pre = 0, ans = 0
        for x in nums {
            pre ^= x
            let a = cnt2[pre ^ target1, default: 0]
            let b = cnt1[pre ^ target2, default: 0]
            ans = (a + b) % MOD
            cnt1[pre, default: 0] = (cnt1[pre, default: 0] + a) % MOD
            cnt2[pre, default: 0] = (cnt2[pre, default: 0] + b) % MOD
        }
        return ans
    }
}
