// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

class Solution {
    fun powerUpdate(nums: IntArray, p: Int, queries: Array<IntArray>): IntArray {
        val mod = 1000000007L
        var vals = IntArray(nums.size + queries.size)
        for (i in nums.indices) vals[i] = nums[i]
        for (i in queries.indices) vals[nums.size + i] = queries[i][0]
        vals.sort()
        var uniq = 0
        for (i in vals.indices) {
            if (uniq == 0 || vals[i] != vals[uniq - 1]) vals[uniq++] = vals[i]
        }
        vals = vals.copyOf(uniq)
        val bit = IntArray(vals.size + 1)
        for (x in nums) add(bit, lowerBound(vals, x) + 1)
        val ans = IntArray(queries.size)
        var size = nums.size
        var cur = p.toLong()
        for (i in queries.indices) {
            add(bit, lowerBound(vals, queries[i][0]) + 1)
            size++
            val x = kth(bit, vals, size - queries[i][1] + 1)
            cur = powm(cur, x.toLong(), mod)
            ans[i] = cur.toInt()
        }
        return ans
    }

    private fun add(bit: IntArray, i0: Int) {
        var i = i0
        while (i < bit.size) {
            bit[i]++
            i += i and -i
        }
    }

    private fun kth(bit: IntArray, vals: IntArray, rank0: Int): Int {
        var rank = rank0
        var idx = 0
        var step = 1
        while ((step shl 1) < bit.size) step = step shl 1
        while (step > 0) {
            val next = idx + step
            if (next < bit.size && bit[next] < rank) {
                idx = next
                rank -= bit[next]
            }
            step = step shr 1
        }
        return vals[idx]
    }

    private fun lowerBound(vals: IntArray, x: Int): Int {
        var lo = 0
        var hi = vals.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (vals[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }

    private fun powm(a0: Long, e0: Long, mod: Long): Long {
        var a = a0
        var e = e0
        var res = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) res = res * a % mod
            a = a * a % mod
            e = e shr 1
        }
        return res
    }
}
