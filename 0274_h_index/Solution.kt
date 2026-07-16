// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

class Solution {
    fun hIndex(citations: IntArray): Int {
        val buckets = IntArray(citations.size + 1)
        for (citation in citations) {
            buckets[minOf(citation, citations.size)]++
        }
        var total = 0
        for (h in buckets.indices.reversed()) {
            total += buckets[h]
            if (total >= h) {
                return h
            }
        }
        return 0
    }
}
