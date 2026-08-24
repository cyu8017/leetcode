// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution {
    fun maximumBeauty(nums: IntArray, k: Int): Int {
        nums.sort()
        var ans = 0
        var left = 0
        for (right in 0 until nums.size) {
            while (nums[right] - nums[left] > 2 * k) left++
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }
}
