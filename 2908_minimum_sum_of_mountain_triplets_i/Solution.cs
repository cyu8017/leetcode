// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

public class Solution {
    public int MinimumSum(int[] nums) {
        int n = nums.Length, ans = 1 << 30;
        for (int j = 1; j < n - 1; j++) {
            int left = 1 << 30, right = 1 << 30;
            for (int i = 0; i < j; i++)
                if (nums[i] < nums[j] && nums[i] < left) left = nums[i];
            for (int k = j + 1; k < n; k++)
                if (nums[k] < nums[j] && nums[k] < right) right = nums[k];
            if (left < (1 << 30) && right < (1 << 30)) {
                int cand = left + nums[j] + right;
                if (cand < ans) ans = cand;
            }
        }
        return ans == (1 << 30) ? -1 : ans;
    }
}
