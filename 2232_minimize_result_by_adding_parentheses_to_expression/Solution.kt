// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution {
    fun minimizeResult(expression: String): String {
        val plus = expression.indexOf('+')
        val left = expression.substring(0, plus)
        val right = expression.substring(plus + 1)
        var bestVal = Int.MAX_VALUE
        var best = ""
        for (i in left.indices) {
            for (j in 1..right.length) {
                val a = left.substring(0, i)
                val b = left.substring(i)
                val c = right.substring(0, j)
                val d = right.substring(j)
                var v = b.toInt() + c.toInt()
                if (a.isNotEmpty()) v *= a.toInt()
                if (d.isNotEmpty()) v *= d.toInt()
                val cand = "$a($b+$c)$d"
                if (v < bestVal) {
                    bestVal = v
                    best = cand
                }
            }
        }
        return best
    }
}
