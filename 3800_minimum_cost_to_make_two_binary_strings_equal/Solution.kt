// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

class Solution {
    fun minimumCost(s: String, t: String, flipCost: Int, swapCost: Int, crossCost: Int): Long {
        val diff = LongArray(2)
        val n = s.length
        for (i in 0 until n) {
            if (s[i] != t[i]) diff[s[i] - '0']++
        }
        var ans = (diff[0] + diff[1]) * flipCost
        val mx = maxOf(diff[0], diff[1])
        val mn = minOf(diff[0], diff[1])
        ans = minOf(ans, mn * swapCost + (mx - mn) * flipCost)
        val avg = (mx + mn) / 2
        ans = minOf(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost)
        return ans
    }
}
