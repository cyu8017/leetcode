// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution {
    fun createSortedArray(instructions: IntArray): Int {
        val MOD = 1_000_000_007
        val size = (instructions.maxOrNull() ?: 0) + 2
        val bit = IntArray(size + 1)
        fun query(i: Int): Int {
            var idx = i
            var s = 0
            while (idx > 0) {
                s += bit[idx]
                idx -= idx and -idx
            }
            return s
        }
        fun update(i: Int) {
            var idx = i
            while (idx <= size) {
                bit[idx]++
                idx += idx and -idx
            }
        }
        var ans = 0
        for ((i, x) in instructions.withIndex()) {
            ans = (ans + minOf(query(x - 1), i - query(x))) % MOD
            update(x)
        }
        return ans
    }
}
