// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var s: String
    private lateinit var ans: BooleanArray

    private fun isPal(t: String): Boolean {
        var i = 0
        var j = t.length - 1
        while (i < j) {
            if (t[i] != t[j]) return false
            i++
            j--
        }
        return true
    }

    private fun dfsStr(u: Int): String {
        val out = StringBuilder()
        for (v in g[u]) out.append(dfsStr(v))
        out.append(s[u])
        ans[u] = isPal(out.toString())
        return out.toString()
    }

    fun findAnswer(parent: IntArray, s: String): BooleanArray {
        val n = parent.size
        this.s = s
        g = Array(n) { ArrayList() }
        for (i in 1 until n) g[parent[i]].add(i)
        ans = BooleanArray(n)
        dfsStr(0)
        return ans
    }
}
