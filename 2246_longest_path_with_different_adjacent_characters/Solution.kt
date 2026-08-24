// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution {

    var ans: Int = 1

    var g: Array<MutableList<Int>>? = null

    var s: String? = null


    private fun dfs(u: Int): Int {

            var best1 = 0; var best2 = 0
            for (v in g[u]) {
                var lenV = dfs(v)
                if (s[v] == s[u]) continue
                if (lenV > best1) {
                    best2 = best1
                    best1 = lenV
                } else if (lenV > best2) best2 = lenV
            }
            ans = maxOf(ans, 1 + best1 + best2)
            return 1 + best1

    }


    fun longestPath(parent: IntArray, s: String): Int {

            var n = parent.size
            this.s = s
            @SuppressWarnings("unchecked")
            var gg = arrayOfNulls<ArrayList>(n)
            g = gg
            for (i in 0 until n) { g[i] = ArrayList<Int>() }
            for (i in 1 until n) { g[parent[i]].add(i) }
            ans = 1
            dfs(0)
            return ans

    }

}
