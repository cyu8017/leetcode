// LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

class Solution {
    private fun calc(a1: IntArray, t1: IntArray, a2: IntArray, t2: IntArray): Int {
        var minEnd = Int.MAX_VALUE
        for (i in 0 until a1.size) { minEnd = minOf(minEnd, a1[i] + t1[i]) }
        var ans = Int.MAX_VALUE
        for (i in 0 until a2.size) { ans = minOf(ans, maxOf(minEnd, a2[i]) + t2[i]) }
        return ans
    }

    fun earliestFinishTime(landStartTime: IntArray, landDuration: IntArray, waterStartTime: IntArray, waterDuration: IntArray): Int {
        return minOf(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration))
    }
}
