// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

using System;

public class Solution {
    public long Rob(int[] nums, int[] colors) {
        int n = nums.Length;
        long f = 0, g = nums[0];
        for (int i = 1; i < n; i++) {
            if (colors[i - 1] == colors[i]) {
                long nf = Math.Max(f, g);
                g = f + nums[i];
                f = nf;
            } else {
                long nf = Math.Max(f, g);
                g = nf + nums[i];
                f = nf;
            }
        }
        return Math.Max(f, g);
    }
}
