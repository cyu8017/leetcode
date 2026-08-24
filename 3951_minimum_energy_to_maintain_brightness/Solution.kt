// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

class Solution {
    fun minEnergy(n: Int, brightness: Int, intervals: Array<IntArray>): Long {
        intervals.sortBy { it[0] }
        val merged = ArrayList<IntArray>()
        merged.add(intArrayOf(intervals[0][0], intervals[0][1]))
        for (i in 1 until intervals.size) {
            val x = intervals[i]
            val last = merged[merged.size - 1]
            if (last[1] < x[0]) merged.add(intArrayOf(x[0], x[1]))
            else if (x[1] > last[1]) last[1] = x[1]
        }
        var ans = 0L
        for (interval in merged) {
            val m = interval[1] - interval[0] + 1
            ans += ((brightness + 2) / 3).toLong() * m
        }
        return ans
    }
}
