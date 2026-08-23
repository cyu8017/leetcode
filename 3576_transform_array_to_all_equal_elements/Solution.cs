// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

public class Solution {
    public bool CanMakeEqual(int[] nums, int k) {
        bool Check(int target, int kk) {
            int cnt = 0, sign = 1;
            for (int i = 0; i < nums.Length - 1; i++) {
                int x = nums[i] * sign;
                if (x == target) sign = 1;
                else { sign = -1; cnt++; }
            }
            return cnt <= kk && nums[nums.Length - 1] * sign == target;
        }
        return Check(nums[0], k) || Check(-nums[0], k);
    }
}
