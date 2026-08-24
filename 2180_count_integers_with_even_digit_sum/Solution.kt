// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution {
    fun countEven(num: Int): Int {
        var ans: Int = 0
        for (x in 1 until = num) {
            var s: Int = 0, y = x
            while (y > 0) { s += y % 10; y /= 10; }
            if (s % 2 == 0) ans++
        }
        return ans
    }
}
