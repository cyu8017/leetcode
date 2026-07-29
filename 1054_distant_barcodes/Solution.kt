// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

class Solution {
    fun rearrangeBarcodes(barcodes: IntArray): IntArray {
        val count = mutableMapOf<Int, Int>()
        for (v in barcodes) count[v] = count.getOrDefault(v, 0) + 1
        val pairs = count.entries.map { intArrayOf(it.key, it.value) }
            .sortedWith(compareByDescending<IntArray> { it[1] }.thenByDescending { it[0] })
        val n = barcodes.size
        val ans = IntArray(n)
        var idx = 0
        for (p in pairs) {
            repeat(p[1]) {
                ans[idx] = p[0]
                idx += 2
                if (idx >= n) idx = 1
            }
        }
        return ans
    }
}
