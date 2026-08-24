// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

class Solution {
    class BITI(n_: Int) {
        val n = n_
        val c = IntArray(n_ + 1)
        fun upd(x0: Int, d: Int) {
            var x = x0
            while (x <= n) {
                c[x] += d
                x += x and -x
            }
        }
        fun qry(x0: Int): Int {
            var x = x0
            var s = 0
            while (x > 0) {
                s += c[x]
                x -= x and -x
            }
            return s
        }
    }

    class BITL(n_: Int) {
        val n = n_
        val c = LongArray(n_ + 1)
        fun upd(x0: Int, d: Long) {
            var x = x0
            while (x <= n) {
                c[x] += d
                x += x and -x
            }
        }
        fun qry(x0: Int): Long {
            var x = x0
            var s = 0L
            while (x > 0) {
                s += c[x]
                x -= x and -x
            }
            return s
        }
    }

    private fun kth(cnt: BITI, m: Int, k0: Int): Int {
        var k = k0
        var idx = 0
        var bit = 1 shl 20
        while (bit != 0) {
            val nidx = idx + bit
            if (nidx <= m && cnt.c[nidx] < k) {
                k -= cnt.c[nidx]
                idx = nidx
            }
            bit = bit shr 1
        }
        return idx + 1
    }

    private fun sumSmallest(cnt: BITI, sum: BITL, uniq: IntArray, m: Int, kk: Int): Long {
        if (kk <= 0) return 0
        val r = kth(cnt, m, kk)
        val before = cnt.qry(r - 1)
        var s = sum.qry(r - 1)
        s += (kk - before).toLong() * uniq[r - 1]
        return s
    }

    private fun rankOf(uniq: IntArray, v: Int): Int {
        var lo = 0
        var hi = uniq.size - 1
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            when {
                uniq[mid] == v -> return mid
                uniq[mid] < v -> lo = mid + 1
                else -> hi = mid - 1
            }
        }
        return lo
    }

    fun minimumCost(nums: IntArray, k0: Int, dist: Int): Long {
        var k = k0 - 1
        val n = nums.size
        var uniq = nums.copyOf()
        uniq.sort()
        var write = 0
        for (i in uniq.indices) {
            if (write == 0 || uniq[i] != uniq[write - 1]) uniq[write++] = uniq[i]
        }
        uniq = uniq.copyOf(write)
        val m = uniq.size
        val cnt = BITI(m + 2)
        val sum = BITL(m + 2)
        for (i in 1..minOf(dist + 1, n - 1)) {
            val r = rankOf(uniq, nums[i]) + 1
            cnt.upd(r, 1)
            sum.upd(r, nums[i].toLong())
        }
        val end = minOf(dist + 1, n - 1)
        var kk = minOf(k, end)
        var ans = nums[0].toLong() + sumSmallest(cnt, sum, uniq, m, kk)
        for (i in dist + 2 until n) {
            val rem = nums[i - dist - 1]
            val r1 = rankOf(uniq, rem) + 1
            cnt.upd(r1, -1)
            sum.upd(r1, -rem.toLong())
            val add = nums[i]
            val r2 = rankOf(uniq, add) + 1
            cnt.upd(r2, 1)
            sum.upd(r2, add.toLong())
            kk = minOf(k, dist + 1)
            ans = minOf(ans, nums[0].toLong() + sumSmallest(cnt, sum, uniq, m, kk))
        }
        return ans
    }
}
