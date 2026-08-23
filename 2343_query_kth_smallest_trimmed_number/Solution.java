// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

import java.util.Arrays;

class Solution {
    public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        int n = nums.length, m = queries.length;
        int[] ans = new int[m];
        for (int qi = 0; qi < m; qi++) {
            int k = queries[qi][0], trim = queries[qi][1];
            String[][] arr = new String[n][2];
            for (int i = 0; i < n; i++) {
                String s = nums[i];
                arr[i][0] = s.substring(s.length() - trim);
                arr[i][1] = String.valueOf(i);
            }
            Arrays.sort(arr, (a, b) -> {
                int c = a[0].compareTo(b[0]);
                if (c != 0) return c;
                return Integer.compare(Integer.parseInt(a[1]), Integer.parseInt(b[1]));
            });
            ans[qi] = Integer.parseInt(arr[k - 1][1]);
        }
        return ans;
    }
}
