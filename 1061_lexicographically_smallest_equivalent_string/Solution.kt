// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution {
    fun smallestEquivalentString(s1: String, s2: String, baseStr: String): String {
        val parent = IntArray(26) { it }
        for (i in s1.indices) union(parent, s1[i] - 'a', s2[i] - 'a')
        return buildString {
            for (ch in baseStr) append(('a'.code + find(parent, ch - 'a')).toChar())
        }
    }

    private fun find(parent: IntArray, x: Int): Int {
        var cur = x
        while (parent[cur] != cur) {
            parent[cur] = parent[parent[cur]]
            cur = parent[cur]
        }
        return cur
    }

    private fun union(parent: IntArray, a: Int, b: Int) {
        val ra = find(parent, a)
        val rb = find(parent, b)
        if (ra == rb) return
        if (ra < rb) parent[rb] = ra else parent[ra] = rb
    }
}
