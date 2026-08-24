// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

class Solution {
    lateinit var graph: Array<ArrayList<Int>>
    lateinit var nums: IntArray
    lateinit var parent: IntArray
    var k = 0
    lateinit var memo: HashMap<String, Long>

    fun subtreeInversionSum(edges: Array<IntArray>, nums: IntArray, k: Int): Long {
        val n = edges.size + 1
        this.nums = nums
        this.k = k
        graph = Array(n) { ArrayList() }
        for (e in edges) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        parent = IntArray(n) { -1 }
        memo = HashMap()
        return dp(0, k, false)
    }

    fun dp(u: Int, steps: Int, inv: Boolean): Long {
        val key = "$u,$steps,$inv"
        memo[key]?.let { return it }
        var num = nums[u].toLong()
        if (inv) num = -num
        var negNum = -num
        for (v in graph[u]) {
            if (v == parent[u]) continue
            parent[v] = u
            var ns = steps + 1
            if (ns > k) ns = k
            num += dp(v, ns, inv)
            if (steps == k) negNum += dp(v, 1, !inv)
        }
        var res = num
        if (steps == k && negNum > res) res = negNum
        memo[key] = res
        return res
    }
}
