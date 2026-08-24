// LeetCode 3725 - Count Ways To Choose Coprime Integers From Rows
// https://leetcode.com/problems/count_ways_to_choose_coprime_integers_from_rows/

class Solution {
    fun countCoprime(mat: Array<IntArray>): Int {
        val MOD = 1_000_000_007
        val m = mat.size
        var dp = HashMap<Int, Int>()
        for (v in mat[0]) {
            dp[v] = dp.getOrDefault(v, 0) + 1
        }
        for (i in 1 until m) {
            val ndp = HashMap<Int, Int>()
            for (v in mat[i]) {
                for ((key, value) in dp) {
                    val ng = gcd(key, v)
                    ndp[ng] = (ndp.getOrDefault(ng, 0) + value) % MOD
                }
            }
            dp = ndp
        }
        return dp.getOrDefault(1, 0)
    }

    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }
}
