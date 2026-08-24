// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

class Solution {
    fun getFactors(n: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val path = mutableListOf<Int>()

        fun backtrack(remain: Int, start: Int) {
            if (start > remain) {
                if (path.size > 1) {
                    result.add(path.toList())
                }
                return
            }

            var factor = start
            while (factor * factor <= remain) {
                if (remain % factor == 0) {
                    path.add(factor)
                    backtrack(remain / factor, factor)
                    path.removeAt(path.size - 1)
                }
                factor += 1
            }

            if (path.isNotEmpty()) {
                path.add(remain)
                if (path.size > 1) {
                    result.add(path.toList())
                }
                path.removeAt(path.size - 1)
            }
        }

        backtrack(n, 2)
        return result
    }
}
