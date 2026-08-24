// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

class Solution {
    fun countOfAtoms(formula: String): String {
        val st = ArrayDeque<TreeMap<String, Int>>()
        st.addLast(TreeMap())
        var i = 0
        val n = formula.length
        while (i < n) {
            when {
                formula[i] == '(' -> {
                    st.addLast(TreeMap())
                    i++
                }
                formula[i] == ')' -> {
                    i++
                    val start = i
                    while (i < n && formula[i].isDigit()) i++
                    val mult = if (start < i) formula.substring(start, i).toInt() else 1
                    val top = st.removeLast()
                    val peek = st.last()
                    for ((key, value) in top) {
                        peek[key] = peek.getOrDefault(key, 0) + value * mult
                    }
                }
                else -> {
                    var start = i++
                    while (i < n && formula[i].isLowerCase()) i++
                    val atom = formula.substring(start, i)
                    start = i
                    while (i < n && formula[i].isDigit()) i++
                    val count = if (start < i) formula.substring(start, i).toInt() else 1
                    val peek = st.last()
                    peek[atom] = peek.getOrDefault(atom, 0) + count
                }
            }
        }
        val result = StringBuilder()
        for ((key, value) in st.last()) {
            result.append(key)
            if (value > 1) result.append(value)
        }
        return result.toString()
    }
}
