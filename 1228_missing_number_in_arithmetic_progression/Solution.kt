// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

class Solution {
    fun missingNumber(arr: IntArray): Int {
        val diff = (arr.last() - arr[0]) / arr.size
        for (i in 1 until arr.size) {
            val expected = arr[0] + i * diff
            if (arr[i] != expected) return expected
        }
        return arr[0]
    }
}
