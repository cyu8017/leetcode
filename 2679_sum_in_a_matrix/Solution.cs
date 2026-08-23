// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

using System;

public class Solution {
    public int MatrixSum(int[][] nums) {
        foreach (var row in nums) Array.Sort(row);
        int ans = 0, n = nums[0].Length;
        for (int j = 0; j < n; j++) {
            int mx = 0;
            foreach (var row in nums) mx = Math.Max(mx, row[j]);
            ans += mx;
        }
        return ans;
    }
}
