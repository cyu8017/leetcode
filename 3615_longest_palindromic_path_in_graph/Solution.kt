// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

class Solution {
    private fun expandPal(g: Array<ArrayList<Int>>, label: String, l: Int, r: Int): Int {
        val vis = HashSet<Long>()
        val q = ArrayDeque<IntArray>()
        val len0 = if (l != r) 2 else 1
        q.offer(intArrayOf(l, r, len0))
        var best = len0
        vis.add(pack(minOf(l, r), maxOf(l, r)))
        while (q.isNotEmpty()) {
            val cur = q.poll()
            for (a in g[cur[0]]) {
                for (b in g[cur[1]]) {
                    if (a == b || label[a] != label[b]) continue
                    val p = pack(minOf(a, b), maxOf(a, b))
                    if (p in vis) continue
                    vis.add(p)
                    val nl = cur[2] + 2
                    best = maxOf(best, nl)
                    q.offer(intArrayOf(a, b, nl))
                }
            }
        }
        return best
    }

    private fun pack(a: Int, b: Int): Long = (a.toLong() shl 32) or (b.toLong() and 0xffffffffL)

    fun maxLen(n: Int, edges: Array<IntArray>, label: String): Int {
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        var ans = 1
        for (i in 0 until n) {
            ans = maxOf(ans, expandPal(g, label, i, i))
            for (j in g[i]) {
                if (i < j && label[i] == label[j]) {
                    ans = maxOf(ans, expandPal(g, label, i, j))
                }
            }
        }
        return ans
    }
}
