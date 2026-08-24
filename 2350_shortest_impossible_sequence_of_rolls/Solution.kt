// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

class Solution {
    fun shortestSequence(rolls: IntArray, k: Int): Int {
        val seen = HashSet<Int>()
        var ans = 1
        for (r in rolls) {
            seen.add(r)
            if (seen.size == k) {
                ans++
                seen.clear()
            }
        }
        return ans
    }
}
