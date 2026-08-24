// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

class Solution {
    fun countRatioSubarrays(nums: IntArray, a: Int, b: Int): Int {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            var y = 0
            for (j in i until n) {
                y += nums[j] % 2
                var x = j - i + 1 - y
                if (y > 0 && x * b <= y * a) ans++
            }
        }
        return ans
    }
}
