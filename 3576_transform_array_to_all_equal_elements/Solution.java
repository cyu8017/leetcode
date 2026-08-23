// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

class Solution {
    public boolean canMakeEqual(int[] nums, int k) {
        return check(nums, nums[0], k) || check(nums, -nums[0], k);
    }

    boolean check(int[] nums, int target, int kk) {
        int cnt = 0, sign = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            int x = nums[i] * sign;
            if (x == target) sign = 1;
            else {
                sign = -1;
                cnt++;
            }
        }
        return cnt <= kk && nums[nums.length - 1] * sign == target;
    }
}
