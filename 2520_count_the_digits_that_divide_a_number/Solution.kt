// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution {
    fun countDigits(num: Int): Int {
        var ans = 0
        var x = num
        while (x > 0) {
            var d = x % 10
            if (d != 0 && num % d == 0) { ans = ans + 1 }
            x /= 10
        }
        return ans
    }
}
