// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

import java.util.TreeSet

class Solution {
    fun minimumPairRemoval(nums: IntArray): Int {
        val n = nums.size
        var inv = 0
        var ans = 0
        val sl = TreeSet<LongArray> { a, b ->
            if (a[0] != b[0]) a[0].compareTo(b[0]) else a[1].compareTo(b[1])
        }
        val idx = TreeSet<Int>()
        for (i in 0 until n) idx.add(i)
        for (i in 0 until n - 1) {
            if (nums[i] > nums[i + 1]) inv++
            sl.add(longArrayOf(nums[i].toLong() + nums[i + 1], i.toLong()))
        }
        while (inv > 0) {
            ans++
            val p = sl.pollFirst()!!
            val s = p[0].toInt()
            val i = p[1].toInt()
            val j = idx.ceiling(i + 1)!!
            if (nums[i] > nums[j]) inv--
            val h = idx.floor(i - 1)
            if (h != null) {
                if (nums[h] > nums[i]) inv--
                sl.remove(longArrayOf(nums[h].toLong() + nums[i], h.toLong()))
                if (nums[h] > s) inv++
                sl.add(longArrayOf(nums[h].toLong() + s, h.toLong()))
            }
            val kk = idx.ceiling(j + 1)
            if (kk != null) {
                if (nums[j] > nums[kk]) inv--
                sl.remove(longArrayOf(nums[j].toLong() + nums[kk], j.toLong()))
                if (s > nums[kk]) inv++
                sl.add(longArrayOf(s.toLong() + nums[kk], i.toLong()))
            }
            nums[i] = s
            idx.remove(j)
        }
        return ans
    }
}
