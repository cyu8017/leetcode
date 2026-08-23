// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

class Solution {
    public long countQuadruplets(int[] nums) {
        int n = nums.length;
        long ans = 0;
        int[] great = new int[n];
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < j; ++i) {
                if (nums[i] < nums[j]) ans += great[i];
                else if (nums[i] > nums[j]) great[i]++;
            }
        }
        return ans;
    }
}
