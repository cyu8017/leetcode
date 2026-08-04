// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

class Solution {
    public int[] minDifference(int[] nums, int[][] queries) {
        int n = nums.length;
        int[][] pref = new int[n + 1][101];
        for (int i = 0; i < n; i++) {
            System.arraycopy(pref[i], 0, pref[i + 1], 0, 101);
            pref[i + 1][nums[i]]++;
        }
        int[] ans = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int left = queries[q][0], right = queries[q][1];
            int prev = -1, best = Integer.MAX_VALUE;
            for (int value = 1; value <= 100; value++) {
                if (pref[right + 1][value] - pref[left][value] > 0) {
                    if (prev != -1) best = Math.min(best, value - prev);
                    prev = value;
                }
            }
            ans[q] = best == Integer.MAX_VALUE ? -1 : best;
        }
        return ans;
    }
}
