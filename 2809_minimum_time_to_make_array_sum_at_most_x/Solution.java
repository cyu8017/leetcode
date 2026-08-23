// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

import java.util.Arrays;
import java.util.List;

class Solution {
    public int minimumTime(List<Integer> nums1, List<Integer> nums2, int x) {
        int n = nums1.size();
        int[][] arr = new int[n][2];
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            arr[i][0] = nums1.get(i);
            arr[i][1] = nums2.get(i);
            sum1 += nums1.get(i);
            sum2 += nums2.get(i);
        }
        Arrays.sort(arr, (u, v) -> Integer.compare(u[1], v[1]));
        int[] dp = new int[n + 1];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j >= 1; j--) {
                dp[j] = Math.max(dp[j], dp[j - 1] + arr[i][0] + j * arr[i][1]);
            }
        }
        for (int t = 0; t <= n; t++) {
            if (sum1 + sum2 * t - dp[t] <= x) return t;
        }
        return -1;
    }
}
