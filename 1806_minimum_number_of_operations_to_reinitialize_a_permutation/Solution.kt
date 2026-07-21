// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

class Solution {
    fun reinitializePermutation(n: Int): Int {
        var perm = IntArray(n) { it }
        val target = IntArray(n) { it }
        var operations = 0
        while (true) {
            val newPerm = IntArray(n)
            for (i in 0 until n) {
                newPerm[i] = if (i % 2 == 0) perm[i / 2] else perm[n / 2 + (i - 1) / 2]
            }
            perm = newPerm
            operations++
            if (perm.contentEquals(target)) return operations
        }
    }
}
