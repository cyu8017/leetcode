// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

class Solution {
    lateinit var parent: IntArray

    fun find(x0: Int): Int {
        var x = x0
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    fun unite(a: Int, b: Int) {
        val ra = find(a)
        val rb = find(b)
        if (ra != rb) {
            if (ra < rb) parent[rb] = ra
            else parent[ra] = rb
        }
    }

    fun processQueries(c: Int, connections: Array<IntArray>, queries: Array<IntArray>): IntArray {
        parent = IntArray(c + 1) { it }
        for (e in connections) unite(e[0], e[1])
        val online = BooleanArray(c + 1) { true }
        val comp = HashMap<Int, ArrayList<Int>>()
        for (i in 1..c) comp.getOrPut(find(i)) { ArrayList() }.add(i)
        for (ids in comp.values) ids.sort()
        val ptr = HashMap<Int, Int>()
        val ans = ArrayList<Int>()
        for (q in queries) {
            val t = q[0]
            val x = q[1]
            if (t == 2) {
                online[x] = false
                continue
            }
            if (online[x]) {
                ans.add(x)
                continue
            }
            val r = find(x)
            val ids = comp[r]!!
            var p = ptr.getOrDefault(r, 0)
            while (p < ids.size && !online[ids[p]]) p++
            ptr[r] = p
            ans.add(if (p < ids.size) ids[p] else -1)
        }
        return ans.toIntArray()
    }
}
