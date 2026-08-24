// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution {

    fun digitCount(num: String): Boolean {

            var cnt = IntArray(10)
            for (c in num.toCharArray()) cnt[c - '0']++
            for (i in 0 until num.length) { if (cnt[i] != num[i] - '0') return false }
            return true

    }

}
