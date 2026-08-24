// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

class Solution {
    fun zigZagArrays(n: Int, l: Int, r: Int): Int {
        val MOD = 1000000007
        val m = r - l + 1
        if (n == 1) return m % MOD
        var up = IntArray(m) { 1 }
        var down = IntArray(m) { 1 }
        for (len_ in 2..n) {
            val prefDown = IntArray(m + 1)
            for (j in 0 until m) prefDown[j + 1] = (prefDown[j] + down[j]) % MOD
            val nup = IntArray(m)
            for (j in 0 until m) nup[j] = prefDown[j]
            val sufUp = IntArray(m + 1)
            for (j in m - 1 downTo 0) sufUp[j] = (sufUp[j + 1] + up[j]) % MOD
            val ndown = IntArray(m)
            for (j in 0 until m) ndown[j] = sufUp[j + 1]
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
