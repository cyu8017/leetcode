// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

class Solution {
    fun sumOfTheDigitsOfHarshadNumber(x: Int): Int {
        var s = 0
        run {
            var y = x
            while (y > 0) {
                s += y % 10
                y /= 10
            }
        }
        return if (x % s == 0) s else -1
    }
}
