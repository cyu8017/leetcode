// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

import java.util.Arrays;

class Solution {
    public int matrixSum(int[][] nums) {
        for (int[] row : nums) Arrays.sort(row);
        int ans = 0, n = nums[0].length;
        for (int j = 0; j < n; j++) {
            int mx = 0;
            for (int[] row : nums) mx = Math.max(mx, row[j]);
            ans += mx;
        }
        return ans;
    }
}
