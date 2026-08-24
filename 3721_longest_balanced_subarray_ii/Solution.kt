// LeetCode 3721 - Longest Balanced Subarray Ii
// https://leetcode.com/problems/longest_balanced_subarray_ii/

class Solution {
    private class Node {
        var l = 0
        var r = 0
        var mn = 0
        var mx = 0
        var lazy = 0
    }

    private class SegmentTree(n: Int) {
        val tr = Array(n shl 2) { Node() }

        init {
            build(1, 0, n)
        }

        fun build(u: Int, l: Int, r: Int) {
            tr[u].l = l
            tr[u].r = r
            tr[u].mn = 0
            tr[u].mx = 0
            tr[u].lazy = 0
            if (l == r) return
            val mid = (l + r) shr 1
            build(u shl 1, l, mid)
            build(u shl 1 or 1, mid + 1, r)
        }

        fun apply(u: Int, v: Int) {
            tr[u].mn += v
            tr[u].mx += v
            tr[u].lazy += v
        }

        fun pushup(u: Int) {
            tr[u].mn = minOf(tr[u shl 1].mn, tr[u shl 1 or 1].mn)
            tr[u].mx = maxOf(tr[u shl 1].mx, tr[u shl 1 or 1].mx)
        }

        fun pushdown(u: Int) {
            if (tr[u].lazy != 0) {
                val v = tr[u].lazy
                apply(u shl 1, v)
                apply(u shl 1 or 1, v)
                tr[u].lazy = 0
            }
        }

        fun modify(u: Int, l: Int, r: Int, v: Int) {
            if (tr[u].l >= l && tr[u].r <= r) {
                apply(u, v)
                return
            }
            pushdown(u)
            val mid = (tr[u].l + tr[u].r) shr 1
            if (l <= mid) modify(u shl 1, l, r, v)
            if (r > mid) modify(u shl 1 or 1, l, r, v)
            pushup(u)
        }

        fun query(u: Int, target: Int): Int {
            if (tr[u].l == tr[u].r) return tr[u].l
            pushdown(u)
            val left = u shl 1
            val right = u shl 1 or 1
            if (tr[left].mn <= target && target <= tr[left].mx) return query(left, target)
            return query(right, target)
        }
    }

    fun longestBalanced(nums: IntArray): Int {
        val n = nums.size
        val st = SegmentTree(n)
        val last = HashMap<Int, Int>()
        var now = 0
        var ans = 0
        for (i in 1..n) {
            val x = nums[i - 1]
            val det = if ((x and 1) != 0) 1 else -1
            if (last.containsKey(x)) {
                st.modify(1, last[x]!!, n, -det)
                now -= det
            }
            last[x] = i
            st.modify(1, i, n, det)
            now += det
            val pos = st.query(1, now)
            ans = maxOf(ans, i - pos)
        }
        return ans
    }
}
