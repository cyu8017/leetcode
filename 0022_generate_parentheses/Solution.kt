// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

class Solution {
    fun generateParenthesis(n: Int): List<String> {
        val result = mutableListOf<String>()
        val path = StringBuilder()

        fun backtrack(openCount: Int, closeCount: Int) {
            if (path.length == 2 * n) {
                result.add(path.toString())
                return
            }
            if (openCount < n) {
                path.append('(')
                backtrack(openCount + 1, closeCount)
                path.deleteCharAt(path.length - 1)
            }
            if (closeCount < openCount) {
                path.append(')')
                backtrack(openCount, closeCount + 1)
                path.deleteCharAt(path.length - 1)
            }
        }

        backtrack(0, 0)
        return result
    }
}
