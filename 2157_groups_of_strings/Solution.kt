// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

class Solution {
    private val parent = HashMap<Int, Int>()
    private val sz = HashMap<Int, Int>()

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x]!!)
        return parent[x]!!
    }

    private fun unite(a: Int, b: Int) {
        var ra = find(a)
        var rb = find(b)
        if (ra == rb) return
        if (sz[ra]!! < sz[rb]!!) {
            val t = ra
            ra = rb
            rb = t
        }
        parent[rb] = ra
        sz[ra] = sz[ra]!! + sz[rb]!!
    }

    private fun maskOf(w: String): Int {
        var m = 0
        for (c in w) m = m or (1 shl (c - 'a'))
        return m
    }

    fun groupStrings(words: Array<String>): IntArray {
        val freq = HashMap<Int, Int>()
        for (w in words) freq.merge(maskOf(w), 1) { a, b -> a + b }
        for ((k, v) in freq) {
            parent[k] = k
            sz[k] = v
        }
        for (m in freq.keys.toList()) {
            for (b in 0 until 26) {
                if ((m and (1 shl b)) != 0) {
                    val nm = m xor (1 shl b)
                    if (freq.containsKey(nm)) unite(m, nm)
                    for (a in 0 until 26) {
                        if ((nm and (1 shl a)) == 0) {
                            val rm = nm or (1 shl a)
                            if (freq.containsKey(rm)) unite(m, rm)
                        }
                    }
                } else {
                    val nm = m or (1 shl b)
                    if (freq.containsKey(nm)) unite(m, nm)
                }
            }
        }
        var groups = 0
        var maxSize = 0
        val seen = HashSet<Int>()
        for (m in freq.keys) {
            val r = find(m)
            if (seen.add(r)) {
                groups++
                maxSize = maxOf(maxSize, sz[r]!!)
            }
        }
        return intArrayOf(groups, maxSize)
    }
}
