// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var nums: IntArray
    private lateinit var xorv: IntArray
    private lateinit var inT: IntArray
    private lateinit var outT: IntArray
    private var time = 0

    fun minimumScore(nums: IntArray, edges: Array<IntArray>): Int {
        val n = nums.size
        this.nums = nums
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        xorv = IntArray(n)
        inT = IntArray(n)
        outT = IntArray(n)
        time = 0
        dfs(0, -1)
        val total = xorv[0]
        var ans = Int.MAX_VALUE
        for (i in 1 until n) {
            for (j in i + 1 until n) {
                val a: Int; val b: Int; val c: Int
                if (isAncestor(i, j)) {
                    a = xorv[j]; b = xorv[i] xor xorv[j]; c = total xor xorv[i]
                } else if (isAncestor(j, i)) {
                    a = xorv[i]; b = xorv[j] xor xorv[i]; c = total xor xorv[j]
                } else {
                    a = xorv[i]; b = xorv[j]; c = total xor xorv[i] xor xorv[j]
                }
                ans = minOf(ans, maxOf(a, b, c) - minOf(a, b, c))
            }
        }
        return ans
    }

    private fun dfs(u: Int, p: Int) {
        inT[u] = time++
        xorv[u] = nums[u]
        for (v in g[u]) if (v != p) {
            dfs(v, u)
            xorv[u] = xorv[u] xor xorv[v]
        }
        outT[u] = time
    }

    private fun isAncestor(a: Int, b: Int) = inT[a] <= inT[b] && outT[b] <= outT[a]
}
