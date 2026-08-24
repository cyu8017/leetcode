// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

class Solution {
    private var nums1: IntArray? = null
    private var ones: IntArray? = null
    private var lazy: BooleanArray? = null

    fun handleQuery(nums1: IntArray, nums2: IntArray, queries: Array<IntArray>): LongArray {
        this.nums1 = nums1
        var n = nums1.size
        ones = IntArray(4 * n)
        lazy = BooleanArray(4 * n)
        build(1, 0, n - 1)
        var sum2 = 0
        for (x in nums2) { sum2 += x }
        var ans = ArrayList<Long>()
        for (q in queries) {
            if (q[0] == 1) update(1, 0, n - 1, q[1], q[2])
            else if (q[0] == 2) sum2 += (long) q[1] * ones[1]
            else ans.add(sum2)
        }
        var res = LongArray(ans.size)
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }

    private fun build(idx: Int, l: Int, r: Int) {
        if (l == r) {
            ones[idx] = nums1[l]
            return
        }
        var m = (l + r) / 2
        build(idx * 2, l, m)
        build(idx * 2 + 1, m + 1, r)
        ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]
    }

    private fun apply(idx: Int, l: Int, r: Int) {
        ones[idx] = (r - l + 1) - ones[idx]
        lazy[idx] = !lazy[idx]
    }

    private fun push(idx: Int, l: Int, r: Int) {
        if (lazy[idx] && l != r) {
            var m = (l + r) / 2
            apply(idx * 2, l, m)
            apply(idx * 2 + 1, m + 1, r)
            lazy[idx] = false
        }
    }

    private fun update(idx: Int, l: Int, r: Int, ql: Int, qr: Int) {
        if (ql <= l && r <= qr) {
            apply(idx, l, r)
            return
        }
        push(idx, l, r)
        var m = (l + r) / 2
        if (ql <= m) update(idx * 2, l, m, ql, qr)
        if (qr > m) update(idx * 2 + 1, m + 1, r, ql, qr)
        ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]
    }
}
