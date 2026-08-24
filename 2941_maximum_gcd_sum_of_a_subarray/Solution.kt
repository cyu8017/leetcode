// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

class Solution {
    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0; var b = b0
        while (b != 0) { val t = a % b; a = b; b = t }
        return a
    }

    fun maxGcdSum(nums: IntArray, k: Int): Long {
        val n = nums.size
        val pref = LongArray(n + 1)
        for (i in 0 until n) pref[i + 1] = pref[i] + nums[i]
        var ans = 0L
        var st = ArrayList<IntArray>()
        for (i in 0 until n) {
            val nst = ArrayList<IntArray>()
            nst.add(intArrayOf(nums[i], i))
            for (p in st) {
                val g = gcd(p[0], nums[i])
                if (nst[nst.size - 1][0] == g) continue
                nst.add(intArrayOf(g, p[1]))
            }
            st = nst
            for (p in st) {
                val g = p[0]; val idx = p[1]
                if (i - idx + 1 >= k) {
                    val cand = (pref[i + 1] - pref[idx]) * g
                    if (cand > ans) ans = cand
                }
            }
        }
        return ans
    }
}
