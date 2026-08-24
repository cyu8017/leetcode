// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution {
    fun separateDigits(nums: IntArray): IntArray {
        var ans = ArrayList<Int>()
        for (num in nums) {
            var x = num
            var digits = ArrayList<Int>()
            while (x > 0) {
                digits.add(x % 10)
                x /= 10
            }
            run {
                var i = digits.size - 1
                while (i >= 0) {
                    ans.add(digits[i])
                    i = i - 1
                }
            }
        }
        var res = IntArray(ans.size)
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }
}
