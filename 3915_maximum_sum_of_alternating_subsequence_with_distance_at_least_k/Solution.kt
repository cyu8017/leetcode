// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

class Solution {
    private class Fenwick(n: Int) {
        val f = LongArray(n)

        fun update(i0: Int, `val`: Long) {
            var i = i0
            while (i < f.size) {
                f[i] = maxOf(f[i], `val`)
                i += i and -i
            }
        }

        fun preMax(i0: Int): Long {
            var i = i0
            var res = 0L
            while (i > 0) {
                res = maxOf(res, f[i])
                i = i and (i - 1)
            }
            return res
        }
    }

    fun maxAlternatingSum(nums: IntArray, k: Int): Long {
        var sorted = nums.clone()
        sorted.sort()
        var m = 0
        for (i in sorted.indices) {
            if (i == 0 || sorted[i] != sorted[i - 1]) sorted[m++] = sorted[i]
        }
        sorted = sorted.copyOf(m)
        val n = nums.size
        val fInc = LongArray(n)
        val fDec = LongArray(n)
        val inc = Fenwick(m + 1)
        val dec = Fenwick(m + 1)
        var ans = 0L
        val ranks = IntArray(n)
        for (i in 0 until n) {
            val x = nums[i]
            if (i >= k) {
                val j = ranks[i - k]
                inc.update(m - j, fInc[i - k])
                dec.update(j + 1, fDec[i - k])
            }
            var jr = sorted.binarySearch(x)
            if (jr < 0) jr = jr.inv()
            ranks[i] = jr
            fInc[i] = dec.preMax(jr) + x
            fDec[i] = inc.preMax(m - 1 - jr) + x
            ans = maxOf(ans, maxOf(fInc[i], fDec[i]))
        }
        return ans
    }
}
