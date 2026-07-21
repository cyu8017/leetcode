// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

class Solution {
    fun minSideJumps(obstacles: IntArray): Int {
        val inf = Int.MAX_VALUE / 4
        var dp = intArrayOf(1, 0, 1)
        for (obs in obstacles) {
            val blocked = BooleanArray(3) { obs == it + 1 }
            val ndp = intArrayOf(inf, inf, inf)
            for (lane in 0 until 3) {
                if (blocked[lane]) continue
                for (other in 0 until 3) {
                    if (blocked[other] || dp[other] >= inf) continue
                    ndp[lane] = minOf(ndp[lane], dp[other] + if (lane != other) 1 else 0)
                }
            }
            dp = ndp
        }
        return dp.minOrNull()!!
    }
}
