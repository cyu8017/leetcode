// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution {
    private lateinit var parent: IntArray

    fun equationsPossible(equations: Array<String>): Boolean {
parent = IntArray(26)
for (i in 0 until 26) {
parent[i] = i
}
for (eq in equations) {
if (eq[1] == '=') {
parent[find(eq[0] - 'a')] = find(eq[3] - 'a')
}
}
for (eq in equations) {
if (eq[1] == '!' && find(eq[0] - 'a') == find(eq[3] - 'a')) {
return false
}
}
return true
}

    private fun find(x: Int): Int {
return if (parent[x] == x) x else (parent[x] = find(parent[x]))
}
}
