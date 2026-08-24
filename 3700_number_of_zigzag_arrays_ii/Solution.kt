// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

class Solution {
    fun zigZagArrays(n: Int, l: Int, r: Int): Int {
        val MOD = 1000000007
        val m = r - l + 1
        if (n == 1) return m % MOD
        var up = IntArray(m) { 1 }
        var down = IntArray(m) { 1 }
        for (length in 2..n) {
            val pref = IntArray(m + 1)
            for (j in 0 until m) pref[j + 1] = (pref[j] + down[j]) % MOD
            val nup = IntArray(m)
            for (j in 0 until m) nup[j] = pref[j]
            val suf = IntArray(m + 1)
            for (j in m - 1 downTo 0) suf[j] = (suf[j + 1] + up[j]) % MOD
            val ndown = IntArray(m)
            for (j in 0 until m) ndown[j] = suf[j + 1]
            up = nup
            down = ndown
        }
        var ans = 0
        for (j in 0 until m) {
            ans = (ans + up[j]) % MOD
            ans = (ans + down[j]) % MOD
        }
        return ans
    }
}
