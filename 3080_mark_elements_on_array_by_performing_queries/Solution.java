// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

import java.util.Arrays;

class Solution {
    public long[] unmarkedSumArray(int[] nums, int[][] queries) {
        int n = nums.length;
        long s = 0;
        for (int x : nums) s += x;
        boolean[] mark = new boolean[n];
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            arr[i][0] = nums[i];
            arr[i][1] = i;
        }
        Arrays.sort(arr, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        long[] ans = new long[queries.length];
        int j = 0;
        for (int qi = 0; qi < queries.length; qi++) {
            int index = queries[qi][0], k = queries[qi][1];
            if (!mark[index]) {
                mark[index] = true;
                s -= nums[index];
            }
            for (; k > 0 && j < n; j++) {
                if (!mark[arr[j][1]]) {
                    mark[arr[j][1]] = true;
                    s -= arr[j][0];
                    k--;
                }
            }
            ans[qi] = s;
        }
        return ans;
    }
}
