// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution {
    fun findSpecialInteger(arr: IntArray): Int {
        val n = arr.size
        val threshold = n / 4
        for (idx in intArrayOf(n / 4, n / 2, 3 * n / 4)) {
            val value = arr[idx]
            var count = 0
            for (x in arr) if (x == value) count++
            if (count > threshold) return value
        }
        return arr[0]
    }
}
