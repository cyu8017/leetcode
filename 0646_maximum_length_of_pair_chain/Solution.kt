// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/


class Solution {
    fun findLongestChain(pairs: Array<IntArray>): Int {
        pairs.sortBy { it[1] }
        var cur = Int.MIN_VALUE
        var count = 0
        for (p in pairs) {
            if (p[0] > cur) {
                count++
                cur = p[1]
            }
        }
        return count
    }
}
