// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var guessSet: HashSet<Long>
    private var ans = 0
    private var k = 0

    fun rootCount(edges: Array<IntArray>, guesses: Array<IntArray>, k: Int): Int {
        this.k = k
        val n = edges.size + 1
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        guessSet = HashSet()
        for (gu in guesses) guessSet.add(pack(gu[0], gu[1]))
        val baseCnt = dfs1(0, -1)
        ans = 0
        dfs2(0, -1, baseCnt)
        return ans
    }

    private fun pack(a: Int, b: Int): Long = (a.toLong() shl 32) or (b.toLong() and 0xffffffffL)

    private fun dfs1(u: Int, p: Int): Int {
        var cnt = 0
        for (v in g[u]) {
            if (v == p) continue
            if (pack(u, v) in guessSet) cnt += 1
            cnt += dfs1(v, u)
        }
        return cnt
    }

    private fun dfs2(u: Int, p: Int, cur: Int) {
        if (cur >= k) ans += 1
        for (v in g[u]) {
            if (v == p) continue
            var nxt = cur
            if (pack(u, v) in guessSet) nxt -= 1
            if (pack(v, u) in guessSet) nxt += 1
            dfs2(v, u, nxt)
        }
    }
}
