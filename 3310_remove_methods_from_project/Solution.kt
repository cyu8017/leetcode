// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var sus: BooleanArray

    private fun dfs(u: Int) {
        if (sus[u]) return
        sus[u] = true
        for (v in g[u]) dfs(v)
    }

    fun remainingMethods(n: Int, k: Int, invocations: Array<IntArray>): List<Int> {
        g = Array(n) { ArrayList() }
        for (e in invocations) g[e[0]].add(e[1])
        sus = BooleanArray(n)
        dfs(k)
        for (e in invocations) {
            if (!sus[e[0]] && sus[e[1]]) {
                val ans = ArrayList<Int>()
                for (i in 0 until n) ans.add(i)
                return ans
            }
        }
        val ans = ArrayList<Int>()
        for (i in 0 until n) if (!sus[i]) ans.add(i)
        return ans
    }
}
