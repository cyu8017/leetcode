// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

class Solution {
    fun minimumFinishTime(tires: Array<IntArray>, changeTime: Int, numLaps: Int): Int {
        var minTime: IntArray = IntArray(20)
        minTime.fill(1 << 30)
        for (tire in tires) {
            var f: Int = tire[0], r = tire[1]
            var t: Long = f, lap = f
            for (x in 1 until 20 && t < minTime[x]) {
                minTime[x] = t
                lap *= r
                if (lap > changeTime + f) break
                t += lap
            }
        }
        var dp: IntArray = IntArray(numLaps + 1)
        dp.fill(1 << 30)
        dp[0] = -changeTime
        for (i in 1 until = numLaps)
            for (j in 1 until = i && j < 20)
                dp[i] = minOf(dp[i], dp[i - j] + changeTime + minTime[j])
        return dp[numLaps]
    }
}
