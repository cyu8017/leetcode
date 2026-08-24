// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

class Solution {
    private var parent: IntArray? = null

    fun numSimilarGroups(strs: Array<String>): Int {
        var n = strs.size
        parent = IntArray(n)
        for (i in 0 until n) { parent[i] = i }
        var groups = n
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (similar(strs[i], strs[j])) {
                    var pi = find(i), pj = find(j)
                    if (pi != pj) {
                        parent[pi] = pj
                        groups--
                    }
                }
            }
        }
        return groups
    }

    private fun find(x: Int): Int {
        var x = x
        while (parent[x] != x) {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    private fun similar(a: String, b: String): Boolean {
        var d0 = -1
        var d1 = -1
        var diffs = 0
        for (i in 0 until a.length) {
            if (a[i] != b[i]) {
                diffs++
                if (diffs > 2) return false
                if (d0 < 0) d0 = i
                else d1 = i
            }
        }
        return diffs == 0 || (diffs == 2 && a[d0] == b[d1] && a[d1] == b[d0])
    }
}
