// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

public class Solution {
    public bool CanChoose(int[][] groups, int[] nums) {
        return Dfs(groups, nums, 0, 0);
    }

    private bool Dfs(int[][] groups, int[] nums, int i, int start) {
        int n = nums.Length;
        if (i == groups.Length) {
            return start == n;
        }
        int[] g = groups[i];
        int m = g.Length;
        for (int j = start; j <= n - m; j++) {
            if (Matches(nums, j, g) && Dfs(groups, nums, i + 1, j + m)) {
                return true;
            }
        }
        return false;
    }

    private bool Matches(int[] nums, int start, int[] g) {
        for (int t = 0; t < g.Length; t++) {
            if (nums[start + t] != g[t]) {
                return false;
            }
        }
        return true;
    }
}
