// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

class Solution {
    fun countSubgraphsForEachDiameter(n: Int, edges: Array<IntArray>): IntArray {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0] - 1
            val b = e[1] - 1
            adj[a].add(b)
            adj[b].add(a)
        }
        val ans = IntArray(n - 1)
        for (mask in 1 until (1 shl n)) {
            if (mask and (mask - 1) == 0) continue
            val start = Integer.numberOfTrailingZeros(mask)
            fun bfs(src: Int): Pair<Int, Map<Int, Int>> {
                val dist = HashMap<Int, Int>()
                dist[src] = 0
                val q = ArrayDeque<Int>()
                q.add(src)
                while (q.isNotEmpty()) {
                    val u = q.removeFirst()
                    for (v in adj[u]) {
                        if ((mask shr v) and 1 == 1 && v !in dist) {
                            dist[v] = dist[u]!! + 1
                            q.add(v)
                        }
                    }
                }
                val far = dist.maxByOrNull { it.value }!!.key
                return far to dist
            }
            val (far, seen) = bfs(start)
            if (seen.size == Integer.bitCount(mask)) {
                val (_, dist) = bfs(far)
                ans[dist.values.maxOrNull()!! - 1]++
            }
        }
        return ans
    }
}
