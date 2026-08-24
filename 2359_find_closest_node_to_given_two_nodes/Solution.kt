// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

class Solution {
    fun closestMeetingNode(edges: IntArray, node1: Int, node2: Int): Int {
        val n = edges.size
        fun dist(start: Int): IntArray {
            val d = IntArray(n) { -1 }
            var cur = start
            var step = 0
            while (cur != -1 && d[cur] == -1) {
                d[cur] = step
                cur = edges[cur]
                step++
            }
            return d
        }
        val d1 = dist(node1)
        val d2 = dist(node2)
        var ans = -1
        var best = Int.MAX_VALUE
        for (i in 0 until n) {
            if (d1[i] == -1 || d2[i] == -1) continue
            val mx = maxOf(d1[i], d2[i])
            if (mx < best) {
                best = mx
                ans = i
            }
        }
        return ans
    }
}
