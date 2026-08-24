// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private var vis = 0
    private var m = 0

    fun evenSumSubgraphs(nums: IntArray, edges: Array<IntArray>): Int {
        val n = nums.size
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        m = (1 shl n) - 1
        var ans = 0
        for (sub in 1..m) {
            var s = 0
            for (i in 0 until n) {
                if (((sub shr i) and 1) != 0) s += nums[i]
            }
            if (s % 2 != 0) continue
            vis = m xor sub
            val start = 31 - Integer.numberOfLeadingZeros(sub)
            dfs(start)
            if (vis == m) ans++
        }
        return ans
    }

    private fun dfs(u: Int) {
        vis = vis or (1 shl u)
        for (v in g[u]) {
            if (((vis shr v) and 1) == 0) dfs(v)
        }
    }
}
