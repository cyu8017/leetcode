// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

class Solution {
    private val MOD = 1000000007

    private fun group(p: IntArray): Int {
        if (p[1] == 0) return 0
        if (p[0] > 0) return 1
        return 2
    }

    fun maxValue(nums1: IntArray, nums0: IntArray): Int {
        val n = nums1.size
        val pairs = Array(n) { IntArray(2) }
        var b = 0
        for (i in 0 until n) {
            pairs[i][0] = nums1[i]
            pairs[i][1] = nums0[i]
            b += nums1[i] + nums0[i]
        }
        pairs.sortWith { a, c ->
            val g1 = group(a)
            val g2 = group(c)
            when {
                g1 != g2 -> g1.compareTo(g2)
                g1 == 0 -> c[0].compareTo(a[0])
                g1 == 1 -> if (a[0] != c[0]) c[0].compareTo(a[0]) else a[1].compareTo(c[1])
                else -> a[1].compareTo(c[1])
            }
        }
        val p = IntArray(b)
        p[0] = 1
        for (i in 1 until b) p[i] = ((2L * p[i - 1]) % MOD).toInt()
        var ans = 0
        b--
        for (pr in pairs) {
            var cnt1 = pr[0]
            var cnt0 = pr[1]
            while (cnt1 > 0) {
                ans = (ans + p[b]) % MOD
                b--
                cnt1--
            }
            b -= cnt0
        }
        return ans
    }
}
