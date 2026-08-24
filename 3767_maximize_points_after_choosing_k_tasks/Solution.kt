// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize_points_after_choosing_k_tasks/

class Solution {
    fun maxPoints(technique1: IntArray, technique2: IntArray, k: Int): Long {
        val n = technique1.size
        val idx = Array(n) { it }
        idx.sortByDescending { technique1[it] - technique2[it] }
        var ans = 0L
        for (x in technique2) ans += x
        for (i in 0 until k) {
            val index = idx[i]
            ans -= technique2[index]
            ans += technique1[index]
        }
        for (i in k until n) {
            val index = idx[i]
            if (technique1[index] >= technique2[index]) {
                ans -= technique2[index]
                ans += technique1[index]
            }
        }
        return ans
    }
}
