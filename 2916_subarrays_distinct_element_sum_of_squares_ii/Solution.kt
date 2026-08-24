// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/


class Solution {
    private val MOD = 1_000_000_007
    private lateinit var tree: Array<Node>

    private class Node {
        var sum = 0
        var sumSq = 0
        var lazy = 0
    }

    fun sumCounts(nums: IntArray): Int {
        val n = nums.size
        val last = HashMap<Int, Int>()
        tree = Array(4 * (n + 2)) { Node() }
        var ans = 0
        for (i in 1..n) {
            val v = nums[i - 1]
            val prev = last.getOrDefault(v, 0)
            update(1, 1, n, prev + 1, i, 1)
            ans = (ans + tree[1].sumSq) % MOD
            last[v] = i
        }
        return ans
    }

    private fun apply(idx: Int, l: Int, r: Int, `val`: Int) {
        val length = r - l + 1
        tree[idx].sumSq = ((tree[idx].sumSq + 2L * `val` % MOD * tree[idx].sum % MOD
                + 1L * `val` % MOD * `val` % MOD * length % MOD) % MOD).toInt()
        tree[idx].sum = ((tree[idx].sum + 1L * `val` % MOD * length % MOD) % MOD).toInt()
        tree[idx].lazy = (tree[idx].lazy + `val`) % MOD
    }

    private fun update(idx: Int, l: Int, r: Int, ql: Int, qr: Int, `val`: Int) {
        if (ql > r || qr < l) return
        if (ql <= l && r <= qr) {
            apply(idx, l, r, `val`)
            return
        }
        if (tree[idx].lazy != 0 && l != r) {
            val mid = (l + r) / 2
            apply(idx * 2, l, mid, tree[idx].lazy)
            apply(idx * 2 + 1, mid + 1, r, tree[idx].lazy)
            tree[idx].lazy = 0
        }
        val mid = (l + r) / 2
        update(idx * 2, l, mid, ql, qr, `val`)
        update(idx * 2 + 1, mid + 1, r, ql, qr, `val`)
        tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % MOD
        tree[idx].sumSq = (tree[idx * 2].sumSq + tree[idx * 2 + 1].sumSq) % MOD
    }
}
