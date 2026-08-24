// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

class Solution {
    private class Fenwick(n: Int) {
        private val bit = IntArray(n)
        fun add(i0: Int, v: Int) {
            var i = i0
            while (i < bit.size) {
                bit[i] += v
                i += i and -i
            }
        }
        fun sum(i0: Int): Int {
            var i = i0
            var s = 0
            while (i > 0) {
                s += bit[i]
                i -= i and -i
            }
            return s
        }
    }

    fun goodTriplets(nums1: IntArray, nums2: IntArray): Long {
        val n = nums1.size
        val pos2 = IntArray(n)
        val mapped = IntArray(n)
        val left = IntArray(n)
        val right = IntArray(n)
        for (i in 0 until n) pos2[nums2[i]] = i
        for (i in 0 until n) mapped[i] = pos2[nums1[i]]
        var fw = Fenwick(n + 2)
        for (i in 0 until n) {
            left[i] = fw.sum(mapped[i])
            fw.add(mapped[i] + 1, 1)
        }
        fw = Fenwick(n + 2)
        for (i in n - 1 downTo 0) {
            right[i] = fw.sum(n) - fw.sum(mapped[i] + 1)
            fw.add(mapped[i] + 1, 1)
        }
        var ans = 0L
        for (i in 0 until n) ans += 1L * left[i] * right[i]
        return ans
    }
}
