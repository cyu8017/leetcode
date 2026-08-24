// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution {
    public int maximumTop(int[] nums, int k) {
        int n = nums.length;
        if (n == 1) return k % 2 != 0 ? -1 : nums[0];
        if (k == 0) return nums[0];
        int ans = -1;
        int limit = Math.min(k - 1, n);
        for (int i = 0; i < limit; i++) ans = Math.max(ans, nums[i]);
        if (k < n) ans = Math.max(ans, nums[k]);
        return ans;
    }
}
