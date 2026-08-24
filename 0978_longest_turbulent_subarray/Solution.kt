// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

class Solution {
    fun maxTurbulenceSize(arr: IntArray): Int {
        var ans = 1
        var cur = 1
        for (i in 1 until arr.size) {
            if (arr[i] == arr[i - 1]) cur = 1
            else if (i == 1 || (arr[i] - arr[i - 1]).toLong() * (arr[i - 1] - arr[i - 2]) < 0) cur++
            else cur = 2
            ans = maxOf(ans, cur)
        }
        return ans
    }
}
