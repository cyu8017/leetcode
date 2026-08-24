// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

class Solution {
    fun shortestDistanceAfterQueries(n: Int, queries: Array<IntArray>): IntArray {
        var nxt = IntArray(n - 1)
        for (i in 0 until n - 1) { nxt[i] = i + 1 }
        var cnt = n - 1
        var ans = ArrayList<Int>()
        for (q in queries) {
            var u = q[0]
            var v = q[1]
            if (nxt[u] > 0 && nxt[u] < v) {
                var i = nxt[u]
                while (i < v) {
                    cnt--
                    var ni = nxt[i]
                    nxt[i] = 0
                    i = ni
                }
                nxt[u] = v
            }
            ans.add(cnt)
        }
        var res = IntArray(ans.size)
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }
}
