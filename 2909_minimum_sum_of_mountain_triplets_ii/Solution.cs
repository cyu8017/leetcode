// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

public class Solution {
    public int MinimumSum(int[] nums) {
        int n = nums.Length;
        int[] left = new int[n], right = new int[n];
        int mn = 1 << 30;
        for (int i = 0; i < n; i++) {
            left[i] = mn;
            if (nums[i] < mn) mn = nums[i];
        }
        mn = 1 << 30;
        for (int i = n - 1; i >= 0; i--) {
            right[i] = mn;
            if (nums[i] < mn) mn = nums[i];
        }
        int ans = 1 << 30;
        for (int j = 1; j < n - 1; j++) {
            if (left[j] < nums[j] && right[j] < nums[j]) {
                int cand = left[j] + nums[j] + right[j];
                if (cand < ans) ans = cand;
            }
        }
        return ans == (1 << 30) ? -1 : ans;
    }
}
