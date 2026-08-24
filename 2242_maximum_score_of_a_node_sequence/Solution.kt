// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

class Solution {

    fun maximumScore(scores: IntArray, edges: Array<IntArray>): Int {

            var n = scores.size
            @SuppressWarnings("unchecked")
            var top = arrayOfNulls<ArrayList>(n)
            @SuppressWarnings("unchecked")
            var g = arrayOfNulls<ArrayList>(n)
            for (i in 0 until n) {
                top[i] = ArrayList<Int>()
                g[i] = ArrayList<Int>()
            }
            for (e in edges) {
                g[e[0]].add(e[1])
                g[e[1]].add(e[0])
            }
            for (i in 0 until n) {
                for (v in g[i]) {
                    top[i].add(v)
                    for (j in (top[i].size - 1) - 1 downTo (0) + 1) {
                        if (scores[top[i][j]] > scores[top[i][j - 1]]) {
                            var tmp = top[i][j]
                            top[i].set(j, top[i][j - 1])
                            top[i].set(j - 1, tmp)
                        }
                    }
                    if (top[i].size > 3) top[i].subList(3, top[i].size).clear()
                }
            }
            var ans = -1
            for (e in edges) {
                var a = e[0]; var b = e[1]
                for (c in top[a]) {
                    if (c == b) continue
                    for (d in top[b]) {
                        if (d == a || d == c) continue
                        ans = maxOf(ans, scores[a] + scores[b] + scores[c] + scores[d])
                    }
                }
            }
            return ans

    }

}
