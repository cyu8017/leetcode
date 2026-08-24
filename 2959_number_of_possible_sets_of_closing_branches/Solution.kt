// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

class Solution {
    fun numberOfSets(n: Int, maxDistance: Int, roads: Array<IntArray>): Int {
        var ans = 0
        for (mask in 0 until (1 shl n)) {
            var dist = IntArray(n)[]
            for (i in 0 until n) {
                dist[i] = IntArray(n)
                for (j in 0 until n) { dist[i][j] = 1 shl 29 }
                dist[i][i] = 0
            }
            for (var r : roads) {
                var u = r[0]
                var v = r[1]
                var w = r[2]
                if ((mask & (1 shl u)) != 0 && (mask & (1 shl v)) != 0) {
                    if (w < dist[u][v]) {
                        dist[u][v] = w
                        dist[v][u] = w
                    }
                }
            }
            for (k in 0 until n) {
                if ((mask & (1 shl k)) == 0) continue
                for (i in 0 until n) {
                    if ((mask & (1 shl i)) == 0) continue
                    for (j in 0 until n) {
                        if ((mask & (1 shl j)) == 0) continue
                        if (dist[i][k] + dist[k][j] < dist[i][j])
                            dist[i][j] = dist[i][k] + dist[k][j]
                    }
                }
            }
            var ok = true
            for (i in 0 until n && ok) {
                if ((mask & (1 shl i)) == 0) continue
                for (j in 0 until n) {
                    if ((mask & (1 shl j)) == 0) continue
                    if (dist[i][j] > maxDistance) { ok = false; break; }
                }
            }
            if (ok) ans++
        }
        return ans
    }
}
