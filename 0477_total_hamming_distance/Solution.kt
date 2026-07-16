// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

class Solution {
    fun totalHammingDistance(nums: IntArray): Int {
        var total = 0
        for (bit in 0 until 32) {
            var zeros = 0
            var ones = 0
            for (value in nums) {
                if (value and (1 shl bit) != 0) {
                    ones++
                } else {
                    zeros++
                }
            }
            total += zeros * ones
        }
        return total
    }
}
