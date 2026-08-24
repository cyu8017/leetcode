// LeetCode 3950 - Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/


class Solution {
    func consecutiveSetBits(_ n: Int) -> Bool {
        var n = n
        var vis = false
        var pre = 0
        while n > 0 {
            let cur = n & 1
            if pre == cur && cur == 1 {
                if vis { return false }
                vis = true
            }
            pre = cur
            n >>= 1
        }
        return vis
    }
}
