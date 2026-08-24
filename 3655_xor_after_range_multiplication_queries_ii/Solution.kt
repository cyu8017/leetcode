// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

class Solution {
    fun xorAfterQueries(nums: IntArray, queries: Array<IntArray>): Int {
        val MOD = 1_000_000_007
        val n = nums.size
        val byK = HashMap<Int, ArrayList<IntArray>>()
        for (q in queries) {
            byK.getOrPut(q[2]) { ArrayList() }.add(intArrayOf(q[0], q[1], q[2], q[3]))
        }
        val res = nums.clone()
        for ((_, list) in byK) {
            val fac = IntArray(n) { 1 }
            for (u in list) {
                var i = u[0]
                while (i <= u[1]) {
                    fac[i] = ((1L * fac[i] * u[3]) % MOD).toInt()
                    i += u[2]
                }
            }
            for (i in 0 until n) res[i] = ((1L * res[i] * fac[i]) % MOD).toInt()
        }
        var ans = 0
        for (v in res) ans = ans xor v
        return ans
    }
}
