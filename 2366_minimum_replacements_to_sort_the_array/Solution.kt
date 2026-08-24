// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution {
    fun minimumReplacement(nums: IntArray): Long {
        var ans = 0L
        val n = nums.size
        var prev = nums[n - 1]
        for (i in n - 2 downTo 0) {
            if (nums[i] <= prev) {
                prev = nums[i]
                continue
            }
            val parts = (nums[i] + prev - 1) / prev
            ans += parts - 1
            prev = nums[i] / parts
        }
        return ans
    }
}
