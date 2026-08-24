// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution {
    fun numOfSubarrays(arr: IntArray): Int {
        val mod = 1_000_000_007
        val counts = intArrayOf(1, 0)
        var parity = 0
        var answer = 0L
        for (value in arr) {
            parity = parity xor (value and 1)
            answer += counts[parity xor 1]
            counts[parity]++
        }
        return (answer % mod).toInt()
    }
}
