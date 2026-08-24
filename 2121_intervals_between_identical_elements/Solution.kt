// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

class Solution {
    fun getDistances(arr: IntArray): LongArray {
        val n = arr.size
        val pos = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) pos.getOrPut(arr[i]) { mutableListOf() }.add(i)
        val ans = LongArray(n)
        for (idxs in pos.values) {
            val m = idxs.size
            val pref = LongArray(m + 1)
            for (i in 0 until m) pref[i + 1] = pref[i] + idxs[i]
            for (i in 0 until m) {
                val left = 1L * i * idxs[i] - pref[i]
                val right = (pref[m] - pref[i + 1]) - 1L * (m - i - 1) * idxs[i]
                ans[idxs[i]] = left + right
            }
        }
        return ans
    }
}
