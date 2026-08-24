// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

import java.util.PriorityQueue

class Solution {
    private fun modPow(a0: Long, e0: Long, mod: Long): Long {
        var a = a0 % mod
        var e = e0
        var r = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) r = r * a % mod
            a = a * a % mod
            e = e shr 1
        }
        return r
    }

    fun getFinalState(nums: IntArray, k0: Int, multiplier: Int): IntArray {
        val mod = 1_000_000_007
        if (multiplier == 1) return nums
        var k = k0
        val cmp = Comparator<IntArray> { a, b ->
            if (a[0] != b[0]) a[0].compareTo(b[0]) else a[1].compareTo(b[1])
        }
        val h = PriorityQueue(cmp)
        var maxV = 0
        for (i in nums.indices) {
            h.offer(intArrayOf(nums[i], i))
            if (nums[i] > maxV) maxV = nums[i]
        }
        while (k > 0 && h.isNotEmpty()) {
            val cur = h.poll()
            val v = cur[0]
            val i = cur[1]
            if (v.toLong() * multiplier > maxV && k >= nums.size) {
                h.offer(intArrayOf(v, i))
                break
            }
            val nv = v * multiplier
            nums[i] = nv
            if (nv > maxV) maxV = nv
            h.offer(intArrayOf(nv, i))
            k--
        }
        if (k > 0) {
            val n = nums.size
            val full = k / n
            val rem = k % n
            val powFull = modPow(multiplier.toLong(), full.toLong(), mod.toLong())
            for (i in 0 until n) {
                nums[i] = (nums[i].toLong() * powFull % mod).toInt()
            }
            val hh = PriorityQueue(cmp)
            for (i in 0 until n) hh.offer(intArrayOf(nums[i], i))
            repeat(rem) {
                val cur = hh.poll()
                val v = (cur[0].toLong() * multiplier % mod).toInt()
                val i = cur[1]
                nums[i] = v
                hh.offer(intArrayOf(v, i))
            }
            for (i in 0 until n) nums[i] %= mod
        } else {
            for (i in nums.indices) nums[i] %= mod
        }
        return nums
    }
}
