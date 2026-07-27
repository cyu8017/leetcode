// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution {
    fun getMaximumGenerated(n: Int): Int {
        if (n < 2) return n
        val a = IntArray(n + 1)
        a[1] = 1
        for (i in 2..n) {
            a[i] = if (i % 2 == 0) a[i / 2] else a[i / 2] + a[i / 2 + 1]
        }
        return a.maxOrNull() ?: 0
    }
}
