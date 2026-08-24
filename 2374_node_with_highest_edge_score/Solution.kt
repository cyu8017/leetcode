// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

class Solution {
    fun edgeScore(edges: IntArray): Int {
        val n = edges.size
        val score = LongArray(n)
        for (i in 0 until n) score[edges[i]] += i.toLong()
        var ans = 0
        for (i in 1 until n) if (score[i] > score[ans]) ans = i
        return ans
    }
}
