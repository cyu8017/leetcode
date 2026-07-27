// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution {
    fun minimumMountainRemovals(nums: IntArray): Int {
        fun lis(a: IntArray): IntArray {
            val d = mutableListOf<Int>()
            val out = IntArray(a.size)
            for (i in a.indices) {
                val x = a[i]
                var lo = 0
                var hi = d.size
                while (lo < hi) {
                    val mid = (lo + hi) ushr 1
                    if (d[mid] < x) lo = mid + 1 else hi = mid
                }
                if (lo == d.size) d.add(x) else d[lo] = x
                out[i] = lo + 1
            }
            return out
        }
        val l = lis(nums)
        val rev = nums.reversedArray()
        val r = lis(rev).reversedArray()
        val n = nums.size
        var best = 0
        for (i in 0 until n) {
            if (l[i] > 1 && r[i] > 1) best = maxOf(best, l[i] + r[i] - 1)
        }
        return n - best
    }
}
