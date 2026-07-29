// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

class Solution {
    fun lastStoneWeightII(stones: IntArray): Int {
        val total = stones.sum()
        var reachable = setOf(0)
        for (stone in stones) {
            val next = mutableSetOf<Int>()
            for (s in reachable) {
                next.add(s)
                next.add(s + stone)
            }
            reachable = next
        }
        var best = total
        for (s in reachable) best = minOf(best, kotlin.math.abs(total - 2 * s))
        return best
    }
}
