// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/


class Solution {
    func minimumCost(_ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        var cnt = 0
        var cur = k
        for x0 in nums {
            let x = x0
            let diff = x - cur
            if diff > 0 {
                let m = (diff + k - 1) / k
                cur += m * k
                cnt += m
            }
            cur -= x
        }
        cnt %= mod
        return ((cnt + 1) * cnt / 2) % mod
    }
}
