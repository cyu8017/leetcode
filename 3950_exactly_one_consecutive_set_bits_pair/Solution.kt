// LeetCode 3950 - Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

class Solution {
    fun consecutiveSetBits(n0: Int): Boolean {
        var n = n0
        var vis = false
        var pre = 0
        while (n > 0) {
            val cur = n and 1
            if (pre == cur && cur == 1) {
                if (vis) return false
                vis = true
            }
            pre = cur
            n = n shr 1
        }
        return vis
    }
}
