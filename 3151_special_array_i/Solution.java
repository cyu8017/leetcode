// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

class Solution {
    public boolean isArraySpecial(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] % 2 == nums[i - 1] % 2) return false;
        }
        return true;
    }
}
