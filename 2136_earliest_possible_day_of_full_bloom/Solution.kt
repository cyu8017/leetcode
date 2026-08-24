// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution {
    fun earliestFullBloom(plantTime: IntArray, growTime: IntArray): Int {
        val n = plantTime.size
        val idx = Array(n) { it }
        idx.sortByDescending { growTime[it] }
        var day = 0
        var ans = 0
        for (i in idx) {
            day += plantTime[i]
            ans = maxOf(ans, day + growTime[i])
        }
        return ans
    }
}
