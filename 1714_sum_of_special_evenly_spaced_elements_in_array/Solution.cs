// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

public class Solution {
    public int[] Solve(int[] nums, int[][] queries) {
        const long mod = 1000000007L;
        int n = nums.Length;
        int block = (int)Math.Sqrt(n) + 1;
        int[][] dp = new int[block][];
        for (int step = 0; step < block; step++) {
            dp[step] = new int[n];
        }
        for (int step = 1; step < block; step++) {
            for (int i = n - 1; i >= 0; i--) {
                long next = i + step < n ? dp[step][i + step] : 0;
                dp[step][i] = (int)((nums[i] + next) % mod);
            }
        }
        int[] ans = new int[queries.Length];
        for (int q = 0; q < queries.Length; q++) {
            int start = queries[q][0];
            int step = queries[q][1];
            if (step < block) {
                ans[q] = dp[step][start];
            } else {
                long total = 0;
                for (int i = start; i < n; i += step) {
                    total += nums[i];
                }
                ans[q] = (int)(total % mod);
            }
        }
        return ans;
    }
}
