// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/


class Solution {
    fun minOperations(s1: String, s2: String, x: Int): Int {
        val diff = ArrayList<Int>()
        for (i in s1.indices) if (s1[i] != s2[i]) diff.add(i)
        val m = diff.size
        if (m % 2 == 1) return -1
        if (m == 0) return 0
        val dp2 = IntArray(m + 1) { 1 shl 30 }
        dp2[0] = 0
        for (i in 0 until m) {
            if (dp2[i] >= (1 shl 30)) continue
            if (i + 1 < m) {
                var cand = diff[i + 1] - diff[i]
                if (cand > x) cand = x
                if (dp2[i] + cand < dp2[i + 2]) dp2[i + 2] = dp2[i] + cand
            }
        }
        return if (dp2[m] >= (1 shl 30)) -1 else dp2[m]
    }
}
