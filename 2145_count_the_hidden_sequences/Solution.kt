// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

class Solution {
    fun numberOfArrays(differences: IntArray, lower: Int, upper: Int): Int {
        var cur: Long = 0, mn = 0, mx = 0
        for (d in differences) {
            cur += d
            mn = minOf(mn, cur)
            mx = maxOf(mx, cur)
        }
        var res: Long = (upper - lower).toLong() - (mx - mn) + 1
        return if (res < 0) 0 else res
    }
}
