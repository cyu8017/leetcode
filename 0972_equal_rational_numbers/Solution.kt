// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

class Solution {
    fun isRationalEqual(s: String, t: String): Boolean {
        return kotlin.math.abs(parse(s) - parse(t)) < 1e-12
    }

    private fun parse(x: String): Double {
        if (!x.contains("(")) return if (x.isEmpty()) 0.0 else x.toDouble()
        val lp = x.indexOf('(')
        var nonRep = x.substring(0, lp)
        val rep = x.substring(lp + 1, x.length - 1)
        if (!nonRep.contains(".")) nonRep += "."
        val dot = nonRep.indexOf('.')
        val integer = nonRep.substring(0, dot)
        val frac = nonRep.substring(dot + 1)
        var bas = if (integer.isEmpty()) 0.0 else integer.toDouble()
        if (frac.isNotEmpty()) {
            var denom = 1.0
            for (i in frac.indices) denom *= 10
            bas += frac.toDouble() / denom
        }
        if (rep.isNotEmpty()) {
            val repVal = rep.toDouble()
            var cycle = 1.0
            for (i in rep.indices) cycle *= 10
            var denom = cycle - 1
            for (i in frac.indices) denom *= 10
            bas += repVal / denom
        }
        return bas
    }
}
