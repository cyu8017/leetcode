// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

class Solution {
    private lateinit var graph: Array<ArrayList<Int>>
    private lateinit var quiet: IntArray
    private lateinit var ans: IntArray

    fun loudAndRich(richer: Array<IntArray>, quiet: IntArray): IntArray {
        val n = quiet.size
        this.quiet = quiet
        graph = Array(n) { ArrayList() }
        for (e in richer) graph[e[1]].add(e[0])
        ans = IntArray(n) { -1 }
        for (i in 0 until n) dfs(i)
        return ans
    }

    private fun dfs(person: Int): Int {
        if (ans[person] != -1) return ans[person]
        var best = person
        for (richerPerson in graph[person]) {
            val cand = dfs(richerPerson)
            if (quiet[cand] < quiet[best]) best = cand
        }
        ans[person] = best
        return best
    }
}
