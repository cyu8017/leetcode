// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

class Solution {
    private lateinit var parent: IntArray

    fun minimumHammingDistance(source: IntArray, target: IntArray, allowedSwaps: Array<IntArray>): Int {
        val n = source.size
        parent = IntArray(n) { it }
        for ((a, b) in allowedSwaps) {
            union(a, b)
        }
        val groups = HashMap<Int, HashMap<Int, Int>>()
        for (i in 0 until n) {
            val counts = groups.getOrPut(find(i)) { HashMap() }
            counts[source[i]] = (counts[source[i]] ?: 0) + 1
        }
        var ans = 0
        for (i in 0 until n) {
            val counts = groups[find(i)]!!
            val remaining = counts[target[i]] ?: 0
            if (remaining > 0) {
                counts[target[i]] = remaining - 1
            } else {
                ans++
            }
        }
        return ans
    }

    private fun find(start: Int): Int {
        var x = start
        while (parent[x] != x) {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    private fun union(a: Int, b: Int) {
        val ra = find(a)
        val rb = find(b)
        if (ra != rb) {
            parent[rb] = ra
        }
    }
}
