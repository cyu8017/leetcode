// LeetCode 1064 - Fixed Point
// https://leetcode.com/problems/fixed-point/

class Solution {
    fun fixedPoint(arr: IntArray): Int {
        var lo = 0
        var hi = arr.lastIndex
        var ans = -1
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            when {
                arr[mid] == mid -> {
                    ans = mid
                    hi = mid - 1
                }
                arr[mid] < mid -> lo = mid + 1
                else -> hi = mid - 1
            }
        }
        return ans
    }
}
