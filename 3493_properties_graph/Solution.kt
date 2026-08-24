// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

class Solution {
    private lateinit var parent: IntArray

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    private fun unite(a: Int, b: Int) {
        val ra = find(a)
        val rb = find(b)
        if (ra != rb) parent[ra] = rb
    }

    fun numberOfComponents(properties: Array<IntArray>, k: Int): Int {
        val n = properties.size
        val sets = Array(n) { HashSet<Int>() }
        for (i in 0 until n) {
            for (v in properties[i]) sets[i].add(v)
        }
        parent = IntArray(n) { it }
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                var cnt = 0
                for (v in sets[i]) if (sets[j].contains(v)) cnt++
                if (cnt >= k) unite(i, j)
            }
        }
        val comp = HashSet<Int>()
        for (i in 0 until n) comp.add(find(i))
        return comp.size
    }
}
