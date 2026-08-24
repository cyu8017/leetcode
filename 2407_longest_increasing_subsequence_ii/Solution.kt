// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

class Solution {
    fun lengthOfLIS(nums: IntArray, k: Int): Int {
        var maxV = 0
        for (x in nums) maxV = maxOf(maxV, x)
        val st = SegTree(maxV + 1)
        var ans = 0
        for (x in nums) {
            val lo = maxOf(1, x - k)
            var best = 1
            if (lo <= x - 1) best = st.query(1, 1, maxV, lo, x - 1) + 1
            st.update(1, 1, maxV, x, best)
            ans = maxOf(ans, best)
        }
        return ans
    }

    private class SegTree(n: Int) {
        private val tree = IntArray(4 * n)

        fun update(idx: Int, l: Int, r: Int, pos: Int, value: Int) {
            if (l == r) {
                tree[idx] = maxOf(tree[idx], value)
                return
            }
            val mid = (l + r) / 2
            if (pos <= mid) update(idx * 2, l, mid, pos, value)
            else update(idx * 2 + 1, mid + 1, r, pos, value)
            tree[idx] = maxOf(tree[idx * 2], tree[idx * 2 + 1])
        }

        fun query(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Int {
            if (qr < l || r < ql) return 0
            if (ql <= l && r <= qr) return tree[idx]
            val mid = (l + r) / 2
            return maxOf(query(idx * 2, l, mid, ql, qr), query(idx * 2 + 1, mid + 1, r, ql, qr))
        }
    }
}
