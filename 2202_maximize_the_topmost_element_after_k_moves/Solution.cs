// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

using System;

public class Solution {
    public int MaximumTop(int[] nums, int k) {
        int n = nums.Length;
        if (n == 1) return k % 2 != 0 ? -1 : nums[0];
        if (k == 0) return nums[0];
        int ans = -1;
        int limit = Math.Min(k - 1, n);
        for (int i = 0; i < limit; i++) ans = Math.Max(ans, nums[i]);
        if (k < n) ans = Math.Max(ans, nums[k]);
        return ans;
    }
}
