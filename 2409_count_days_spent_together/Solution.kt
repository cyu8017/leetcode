// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

class Solution {
    companion object {
        private val DAYS = intArrayOf(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    }

    fun countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int {
        val a1 = toDay(arriveAlice)
        val a2 = toDay(leaveAlice)
        val b1 = toDay(arriveBob)
        val b2 = toDay(leaveBob)
        val start = maxOf(a1, b1)
        val end = minOf(a2, b2)
        if (end < start) return 0
        return end - start + 1
    }

    private fun toDay(s: String): Int {
        val m = (s[0] - '0') * 10 + (s[1] - '0')
        val d = (s[3] - '0') * 10 + (s[4] - '0')
        var res = d
        for (i in 0 until m - 1) res += DAYS[i]
        return res
    }
}
