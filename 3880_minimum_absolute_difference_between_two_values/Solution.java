// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

class Solution {
    public int minAbsoluteDifference(int[] nums) {
        int n = nums.length;
        int ans = n + 1;
        int[] last = { -ans, -ans, -ans };
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (x != 0) {
                ans = Math.min(ans, i - last[3 - x]);
                last[x] = i;
            }
        }
        if (ans > n) return -1;
        return ans;
    }
}
