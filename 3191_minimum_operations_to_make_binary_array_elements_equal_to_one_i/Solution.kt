// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

class Solution {
    fun minOperations(nums: IntArray): Int {
        var ans = 0
        for (i in 0 until nums.size) {
            if (nums[i] == 0) {
                if (i + 2 >= nums.size) return -1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans++
            }
        }
        return ans
    }
}
