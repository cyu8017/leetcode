// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

class Solution {
    private fun modPow(a0: Long, b0: Long, mod: Long): Long {
        var a = a0 % mod
        var b = b0
        var res = 1L % mod
        while (b > 0) {
            if ((b and 1L) != 0L) res = res * a % mod
            a = a * a % mod
            b = b shr 1
        }
        return res
    }

    fun getGoodIndices(variables: Array<IntArray>, target: Int): MutableList<Int> {
        val ans = ArrayList<Int>()
        for (i in variables.indices) {
            val v = variables[i]
            val a = v[0].toLong()
            val b = v[1].toLong()
            val c = v[2].toLong()
            val m = v[3].toLong()
            if (modPow(modPow(a, b, 10), c, m) == target.toLong()) ans.add(i)
        }
        return ans
    }
}
