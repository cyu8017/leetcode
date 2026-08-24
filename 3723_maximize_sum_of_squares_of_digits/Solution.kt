// LeetCode 3723 - Maximize Sum Of Squares Of Digits
// https://leetcode.com/problems/maximize_sum_of_squares_of_digits/

class Solution {
    fun maxSumOfSquares(num: Int, sum: Int): String {
        if (num * 9 < sum) return ""
        var k = sum / 9
        var s = sum % 9
        var ans = StringBuilder()
        for (i in 0 until k) { ans.append('9') }
        if (s > 0) ans.append(('0' + s).toInt().toChar())
        while (ans.length < num) { ans.append('0') }
        return ans.toString()
    }
}
