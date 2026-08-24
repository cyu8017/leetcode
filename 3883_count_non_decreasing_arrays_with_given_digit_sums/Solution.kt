// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

class Solution {
    fun countNonDecreasingArrays(digitSum: IntArray): Int {
        val mod = 1000000007
        val groups = Array(51) { ArrayList<Int>() }
        for (i in 0..50) groups[i] = ArrayList()
        for (x in 0..5000) {
            var s = 0
            var y = x
            while (y > 0) {
                s += y % 10
                y /= 10
            }
            groups[s].add(x)
        }
        var prevVals: ArrayList<Int> = groups[digitSum[0]]
        var dp = IntArray(prevVals.size) { 1 }
        for (pos in 1 until digitSum.size) {
            val curVals = groups[digitSum[pos]]
            val next = IntArray(curVals.size)
            var j = 0
            var prefix = 0
            for (i in curVals.indices) {
                val x = curVals[i]
                while (j < prevVals.size && prevVals[j] <= x) {
                    prefix += dp[j]
                    if (prefix >= mod) prefix -= mod
                    j++
                }
                next[i] = prefix
            }
            prevVals = curVals
            dp = next
        }
        var ans = 0
        for (x in dp) {
            ans += x
            if (ans >= mod) ans -= mod
        }
        return ans
    }
}
