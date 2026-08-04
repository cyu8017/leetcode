// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

class Solution {
    fun findBestValue(arr: IntArray, target: Int): Int {
        var lo = 0
        var hi = arr.maxOrNull()!!
        while (lo < hi) {
            val mid = (lo + hi) / 2
            val s = arr.sumOf { minOf(it, mid) }
            if (s < target) lo = mid + 1 else hi = mid
        }
        val before = arr.sumOf { minOf(it, lo - 1) }
        val after = arr.sumOf { minOf(it, lo) }
        return if (target - before <= after - target) lo - 1 else lo
    }
}
