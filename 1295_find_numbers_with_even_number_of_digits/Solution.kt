// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution {
    fun findNumbers(nums: IntArray): Int {
        var count = 0
        for (value in nums) {
            var digits = if (value == 0) 1 else 0
            var x = value
            while (x > 0) {
                digits++
                x /= 10
            }
            if (digits % 2 == 0) count++
        }
        return count
    }
}
