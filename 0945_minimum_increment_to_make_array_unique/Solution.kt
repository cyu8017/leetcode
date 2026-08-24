// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution {
    fun minIncrementForUnique(nums: IntArray): Int {
        nums.sort()
        var ans = 0
        for (i in 1 until nums.size) {
            if (nums[i] <= nums[i - 1]) {
                var need = nums[i - 1] + 1
                ans += need - nums[i]
                nums[i] = need
            }
        }
        return ans
    }
}
