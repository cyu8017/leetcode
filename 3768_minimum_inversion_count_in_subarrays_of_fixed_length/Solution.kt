// LeetCode 3768 - Minimum Inversion Count In Subarrays Of Fixed Length
// https://leetcode.com/problems/minimum_inversion_count_in_subarrays_of_fixed_length/

class Solution {
    private lateinit var bit: IntArray

    fun minInversionCount(nums: IntArray, k: Int): Long {
        var vals = nums.copyOf()
        vals.sort()
        val u = unique(vals)
        vals = vals.copyOf(u)
        bit = IntArray(vals.size + 1)
        val rank = IntArray(nums.size)
        var inv = 0L
        for (i in nums.indices) {
            rank[i] = lowerBound(vals, nums[i]) + 1
            if (i < k) {
                inv += i - sum(rank[i])
                add(rank[i], 1)
            }
        }
        var best = inv
        for (r in k until nums.size) {
            val left = rank[r - k]
            inv -= sum(left - 1)
            add(left, -1)
            inv += k - 1 - sum(rank[r])
            add(rank[r], 1)
            if (inv < best) best = inv
        }
        return best
    }

    private fun add(i0: Int, delta: Int) {
        var i = i0
        while (i < bit.size) {
            bit[i] += delta
            i += i and -i
        }
    }

    private fun sum(i0: Int): Int {
        var i = i0
        var res = 0
        while (i > 0) {
            res += bit[i]
            i -= i and -i
        }
        return res
    }

    private fun unique(a: IntArray): Int {
        var n = 0
        for (i in a.indices) {
            if (n == 0 || a[i] != a[n - 1]) a[n++] = a[i]
        }
        return n
    }

    private fun lowerBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
