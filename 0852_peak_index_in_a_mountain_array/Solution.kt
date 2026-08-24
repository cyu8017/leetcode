// LeetCode 0852 - Peak Index in a Mountain Array
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution {
    fun peakIndexInMountainArray(arr: IntArray): Int {
        var lo = 0
        var hi = arr.size - 1
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (arr[mid] < arr[mid + 1]) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
