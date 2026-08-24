// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

class Solution {
    fun goodDaysToRobBank(security: IntArray, time: Int): List<Int> {
        val n = security.size
        if (time == 0) return (0 until n).toList()
        val left = IntArray(n)
        val right = IntArray(n)
        for (i in 1 until n) if (security[i] <= security[i - 1]) left[i] = left[i - 1] + 1
        for (i in n - 2 downTo 0) if (security[i] <= security[i + 1]) right[i] = right[i + 1] + 1
        val ans = mutableListOf<Int>()
        for (i in time until n - time) if (left[i] >= time && right[i] >= time) ans.add(i)
        return ans
    }
}
