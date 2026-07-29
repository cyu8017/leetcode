// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

class Solution {
    fun braceExpansionII(expression: String): List<String> {
        val idx = intArrayOf(0)
        val result = parse(expression, idx)
        return result.sorted()
    }

    private fun parse(expr: String, idx: IntArray): Set<String> {
        val union = mutableSetOf<String>()
        var cur = mutableSetOf("")
        while (idx[0] < expr.length && expr[idx[0]] != '}') {
            val c = expr[idx[0]]
            when {
                c == '{' -> {
                    idx[0]++
                    val nested = parse(expr, idx)
                    val next = mutableSetOf<String>()
                    for (a in cur) for (b in nested) next.add(a + b)
                    cur = next
                }
                c == ',' -> {
                    union.addAll(cur)
                    cur = mutableSetOf("")
                    idx[0]++
                }
                else -> {
                    var j = idx[0]
                    while (j < expr.length && expr[j].isLowerCase()) j++
                    val token = expr.substring(idx[0], j)
                    val next = mutableSetOf<String>()
                    for (a in cur) next.add(a + token)
                    cur = next
                    idx[0] = j
                }
            }
        }
        union.addAll(cur)
        idx[0]++ // skip '}'
        return union
    }
}
