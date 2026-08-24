// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

class Solution {
    fun removeInvalidParentheses(s: String): List<String> {
        val result = HashSet<String>()
        val queue = ArrayDeque<String>()
        val visited = HashSet<String>()
        queue.addLast(s)
        visited.add(s)
        var found = false
        while (queue.isNotEmpty()) {
            val levelSize = queue.size
            repeat(levelSize) {
                val current = queue.removeFirst()
                if (isValid(current)) {
                    result.add(current)
                    found = true
                }
                if (found) {
                    return@repeat
                }
                for (index in current.indices) {
                    if (current[index] != '(' && current[index] != ')') {
                        continue
                    }
                    val next = current.substring(0, index) + current.substring(index + 1)
                    if (visited.add(next)) {
                        queue.addLast(next)
                    }
                }
            }
        }
        return result.toList()
    }

    private fun isValid(text: String): Boolean {
        var balance = 0
        for (ch in text) {
            when (ch) {
                '(' -> balance++
                ')' -> {
                    if (balance == 0) {
                        return false
                    }
                    balance--
                }
            }
        }
        return balance == 0
    }
}
