// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

class Solution {
    static class Node {
        var l = 0
        var r = 0
        var s00 = 0
        var s01 = 0
        var s10 = 0
        var s11 = 0
    }

    private Node[] tr

    private fun build(u: Int, l: Int, r: Int) {
        tr[u].l = l
        tr[u].r = r
        if (l == r) return
        var mid = (l + r)  shr  1
        build(u  shl  1, l, mid)
        build(u  shl  1 | 1, mid + 1, r)
    }

    private fun pushup(u: Int) {
        var left = tr[u  shl  1]
        var right = tr[u  shl  1 | 1]
        tr[u].s00 = maxOf(left.s00 + right.s10, left.s01 + right.s00)
        tr[u].s01 = maxOf(left.s00 + right.s11, left.s01 + right.s01)
        tr[u].s10 = maxOf(left.s10 + right.s10, left.s11 + right.s00)
        tr[u].s11 = maxOf(left.s10 + right.s11, left.s11 + right.s01)
    }

    private fun modify(u: Int, x: Int, v: Int) {
        if (tr[u].l == tr[u].r) {
            tr[u].s11 = maxOf(0, v)
            return
        }
        var mid = (tr[u].l + tr[u].r)  shr  1
        if (x <= mid) modify(u  shl  1, x, v)
        else modify(u  shl  1 | 1, x, v)
        pushup(u)
    }

    private fun query(u: Int, l: Int, r: Int): Int {
        if (tr[u].l >= l && tr[u].r <= r) return tr[u].s11
        var mid = (tr[u].l + tr[u].r)  shr  1
        var ans = 0
        if (r <= mid) ans = query(u  shl  1, l, r)
        if (l > mid) ans = maxOf(ans, query(u  shl  1 | 1, l, r))
        return ans
    }

    fun maximumSumSubsequence(nums: IntArray, queries: Array<IntArray>): Int {
        var n = nums.size
        tr = Node[n * 4]
        for (i in 0 until tr.size) { tr[i] = Node() }
        build(1, 1, n)
        for (i in 0 until n) { modify(1, i + 1, nums[i]) }
        val MOD = 1_000_000_007
        var ans = 0
        for (q in queries) {
            modify(1, q[0] + 1, q[1])
            ans = (ans + query(1, 1, n)) % MOD
        }
        return ans
    }
}
