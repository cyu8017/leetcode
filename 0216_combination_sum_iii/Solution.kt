// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

class Solution {
    fun combinationSum3(k: Int, n: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val path = mutableListOf<Int>()

        fun backtrack(start: Int, remaining: Int) {
            if (path.size == k) {
                if (remaining == 0) {
                    result.add(path.toList())
                }
                return
            }
            if (remaining <= 0 || path.size >= k) {
                return
            }

            for (num in start..9) {
                if (num > remaining) {
                    break
                }
                path.add(num)
                backtrack(num + 1, remaining - num)
                path.removeAt(path.size - 1)
            }
        }

        backtrack(1, n)
        return result
    }
}
