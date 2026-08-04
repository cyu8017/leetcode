// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

class Solution {
    public int movesToMakeZigzag(int[] nums) {
        return Math.min(cost(nums, 0), cost(nums, 1));
    }

    private int cost(int[] nums, int start) {
        int ans = 0;
        for (int i = start; i < nums.length; i += 2) {
            int left = i > 0 ? nums[i - 1] : Integer.MAX_VALUE;
            int right = i + 1 < nums.length ? nums[i + 1] : Integer.MAX_VALUE;
            ans += Math.max(0, nums[i] - Math.min(left, right) + 1);
        }
        return ans;
    }
}
