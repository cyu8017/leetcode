// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

class Solution {
    public boolean canChoose(int[][] groups, int[] nums) {
        return dfs(groups, nums, 0, 0);
    }

    private boolean dfs(int[][] groups, int[] nums, int i, int start) {
        int n = nums.length;
        if (i == groups.length) {
            return start == n;
        }
        int[] g = groups[i];
        int m = g.length;
        for (int j = start; j <= n - m; j++) {
            if (matches(nums, j, g) && dfs(groups, nums, i + 1, j + m)) {
                return true;
            }
        }
        return false;
    }

    private boolean matches(int[] nums, int start, int[] g) {
        for (int t = 0; t < g.length; t++) {
            if (nums[start + t] != g[t]) {
                return false;
            }
        }
        return true;
    }
}
