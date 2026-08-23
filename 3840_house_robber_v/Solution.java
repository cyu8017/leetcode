// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

class Solution {
    public long rob(int[] nums, int[] colors) {
        int n = nums.length;
        long f = 0, g = nums[0];
        for (int i = 1; i < n; i++) {
            if (colors[i - 1] == colors[i]) {
                long nf = Math.max(f, g);
                g = f + nums[i];
                f = nf;
            } else {
                long nf = Math.max(f, g);
                g = nf + nums[i];
                f = nf;
            }
        }
        return Math.max(f, g);
    }
}
