// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

class Solution {
    fun simplifyPath(path: String): String {
        val stack = ArrayDeque<String>()

        for (part in path.split("/")) {
            when {
                part.isEmpty() || part == "." -> continue
                part == ".." -> if (stack.isNotEmpty()) stack.removeLast()
                else -> stack.addLast(part)
            }
        }

        return "/" + stack.joinToString("/")
    }
}
