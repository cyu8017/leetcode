// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution {
    fun generateKey(num1: Int, num2: Int, num3: Int): Int {
        var ans = 0
        var mul = 1
        for (t in 0 until 4) {
            var d = minOf(num1 % 10, minOf(num2 % 10, num3 % 10))
            ans += d * mul
            mul *= 10
            num1 /= 10; num2 /= 10; num3 /= 10
        }
        return ans
    }
}
