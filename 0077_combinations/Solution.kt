// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

class Solution {
    fun combine(n: Int, k: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val path = mutableListOf<Int>()

        fun backtrack(start: Int) {
            if (path.size == k) {
                result.add(path.toList())
                return
            }

            val remaining = k - path.size
            for (i in start..(n - remaining + 1)) {
                path.add(i)
                backtrack(i + 1)
                path.removeAt(path.lastIndex)
            }
        }

        backtrack(1)
        return result
    }
}
