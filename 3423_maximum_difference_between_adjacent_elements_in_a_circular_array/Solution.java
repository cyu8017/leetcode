// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int ans = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int d = Math.abs(nums[i] - nums[(i + 1) % n]);
            if (d > ans) ans = d;
        }
        return ans;
    }
}
