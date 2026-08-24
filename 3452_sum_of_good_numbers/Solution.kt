// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

class Solution {
    fun sumOfGoodNumbers(nums: IntArray, k: Int): Int {
        var ans = 0
        var n = nums.size
        for (i in 0 until n) {
            var x = nums[i]
            var good = true
            if (i - k >= 0 && x <= nums[i - k]) good = false
            if (i + k < n && x <= nums[i + k]) good = false
            if (good) ans += x
        }
        return ans
    }
}
