// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

import java.util.ArrayDeque

class Solution {
    fun maximumInvitations(favorite: IntArray): Int {
        var n: Int = favorite.size
        var indeg: IntArray = IntArray(n), depth = IntArray(n)
        depth.fill(1)
        for (f in favorite) indeg[f]++
        var q = ArrayDeque()
        for (i in 0 until n) if (indeg[i] == 0) q.offer(i)
        while (!q.isEmpty()) {
            var u: Int = q.poll()
            var v: Int = favorite[u]
            depth[v] = maxOf(depth[v], depth[u] + 1)
            if (--indeg[v] == 0) q.offer(v)
        }
        var pairSum: Int = 0, maxCycle = 0
        var vis: BooleanArray = BooleanArray(n)
        for (i in 0 until n) {
            if (indeg[i] == 0 || vis[i]) continue
            var u: Int = i, lenCycle = 0
            while (!vis[u]) {
                vis[u] = true
                u = favorite[u]
                lenCycle++
            }
            if (lenCycle == 2) pairSum += depth[i] + depth[favorite[i]]
            else maxCycle = maxOf(maxCycle, lenCycle)
        }
        return maxOf(pairSum, maxCycle)
    }
}
