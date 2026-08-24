// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

class Solution {
    fun countMajoritySubarrays(nums: IntArray, target: Int): Int {
        val n = nums.size
        var ans = 0
        for (i in 0 until n) {
            var cnt = 0
            for (j in i until n) {
                if (nums[j] == target) cnt++
                if (cnt * 2 > j - i + 1) ans++
            }
        }
        return ans
    }
}
