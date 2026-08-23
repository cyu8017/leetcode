// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

// JavaScript problem; Java stand-in.
class Solution {
    public int[][] snail(int[] nums, int rowsCount, int colsCount) {
        if (rowsCount * colsCount != nums.length) return new int[0][];
        int[][] ans = new int[rowsCount][colsCount];
        int idx = 0;
        for (int c = 0; c < colsCount; c++) {
            if (c % 2 == 0) {
                for (int r = 0; r < rowsCount; r++) ans[r][c] = nums[idx++];
            } else {
                for (int r = rowsCount - 1; r >= 0; r--) ans[r][c] = nums[idx++];
            }
        }
        return ans;
    }
}
