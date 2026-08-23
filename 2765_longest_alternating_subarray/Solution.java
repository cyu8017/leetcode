// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

class Solution {
    public int alternatingSubarray(int[] nums) {
        int ans = -1, n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int expect = ((j - i) % 2 == 0) ? -1 : 1;
                if (nums[j] - nums[j - 1] != expect) break;
                if (nums[i + 1] - nums[i] != 1) break;
                ans = Math.max(ans, j - i + 1);
            }
        }
        return ans;
    }
}
