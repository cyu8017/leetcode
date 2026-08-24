// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

class Solution {
    fun countDigitOccurrences(nums: IntArray, digit: Int): Int {
        var ans = 0
        for (num in nums) {
            var x = num
            for (; x > 0; x /= 10) {
                if (x % 10 == digit) ans++
            }
        }
        return ans
    }
}
