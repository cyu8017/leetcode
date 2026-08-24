// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

class Solution {
    fun isValid(code: String): Boolean {
        val stack = ArrayDeque<String>()
        var i = 0
        val n = code.length
        while (i < n) {
            when {
                code.startsWith("<![CDATA[", i) -> {
                    if (stack.isEmpty()) return false
                    val j = code.indexOf("]]>", i + 9)
                    if (j < 0) return false
                    i = j + 3
                }
                code.startsWith("</", i) -> {
                    val j = code.indexOf('>', i + 2)
                    if (j < 0) return false
                    val tag = code.substring(i + 2, j)
                    if (stack.isEmpty() || stack.first() != tag) return false
                    stack.removeFirst()
                    i = j + 1
                    if (stack.isEmpty() && i < n) return false
                }
                code[i] == '<' -> {
                    val j = code.indexOf('>', i + 1)
                    if (j < 0) return false
                    val tag = code.substring(i + 1, j)
                    if (tag.isEmpty() || tag.length > 9) return false
                    for (ch in tag) {
                        if (ch !in 'A'..'Z') return false
                    }
                    stack.addFirst(tag)
                    i = j + 1
                }
                else -> {
                    if (stack.isEmpty()) return false
                    i++
                }
            }
        }
        return stack.isEmpty()
    }
}
