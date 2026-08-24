// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

import java.util.Arrays;

class Solution {
    public int minDeletionSize(String[] strs) {
        int m = strs[0].length();
        int[] dp = new int[m];
        Arrays.fill(dp, 1);
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < j; i++) {
                boolean ok = true;
                for (String row : strs) {
                    if (row.charAt(i) > row.charAt(j)) { ok = false; break; }
                }
                if (ok) dp[j] = Math.max(dp[j], dp[i] + 1);
            }
        }
        int mx = 0;
        for (int x : dp) mx = Math.max(mx, x);
        return m - mx;
    }
}
