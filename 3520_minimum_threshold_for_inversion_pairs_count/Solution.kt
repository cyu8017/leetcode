// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

class Solution {
    fun countInv(nums: IntArray, k: Int, threshold: Int): Boolean {
        var sorted = ArrayList<Int>()
        var inv = 0
        for (num in nums) {
            var left = upperBound(sorted, num)
            var right = upperBound(sorted, num + threshold)
            inv += right - left
            sorted.add(upperBound(sorted, num), num)
        }
        return inv >= k
    }
    fun upperBound(a: MutableList<Int>, target: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (a[mid] <= target) lo = mid + 1
            else hi = mid
        }
        return lo
    }
    fun minThreshold(nums: IntArray, k: Int): Int {
        var mx = 0
        for (v in nums) { if (v > mx) mx = v }
        var l = 0
        var r = mx + 1
        while (l < r) {
            var m = (l + r) / 2
            if (countInv(nums, k, m)) r = m
            else l = m + 1
        }
        return if (l > mx) -1 else l
    }
}
