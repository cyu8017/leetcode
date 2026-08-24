// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var rg: Array<ArrayList<Int>>
    private lateinit var vis: BooleanArray
    private lateinit var order: ArrayList<Int>
    private lateinit var comp: IntArray
    private var cid = 0

    private fun dfs1(u: Int) {
        vis[u] = true
        for (v in g[u]) if (!vis[v]) dfs1(v)
        order.add(u)
    }

    private fun dfs2(u: Int) {
        comp[u] = cid
        for (v in rg[u]) if (comp[v] == -1) dfs2(v)
    }

    fun minRunesToAdd(n: Int, crystals: IntArray, flowFrom: IntArray, flowTo: IntArray): Int {
        g = Array(n) { ArrayList() }
        rg = Array(n) { ArrayList() }
        for (i in flowFrom.indices) {
            val a = flowFrom[i]
            val b = flowTo[i]
            g[a].add(b)
            rg[b].add(a)
        }
        vis = BooleanArray(n)
        order = ArrayList()
        for (i in 0 until n) if (!vis[i]) dfs1(i)
        comp = IntArray(n) { -1 }
        cid = 0
        for (i in n - 1 downTo 0) {
            val u = order[i]
            if (comp[u] == -1) {
                dfs2(u)
                cid++
            }
        }
        val hasCrystal = BooleanArray(cid)
        for (c in crystals) hasCrystal[comp[c]] = true
        val indeg = IntArray(cid)
        for (u in 0 until n) {
            for (v in g[u]) {
                if (comp[u] != comp[v]) indeg[comp[v]]++
            }
        }
        var ans = 0
        for (i in 0 until cid) {
            if (indeg[i] == 0 && !hasCrystal[i]) ans++
        }
        return ans
    }
}
