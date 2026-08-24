// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution {
    fun sumOddLengthSubarrays(arr: IntArray): Int {
        val n = arr.size
        var ans = 0
        for (i in 0 until n) {
            ans += arr[i] * (((i + 1) * (n - i) + 1) / 2)
        }
        return ans
    }
}
