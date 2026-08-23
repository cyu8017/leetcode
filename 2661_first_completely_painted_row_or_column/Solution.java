// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[] posR = new int[m * n + 1], posC = new int[m * n + 1];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                posR[mat[i][j]] = i;
                posC[mat[i][j]] = j;
            }
        int[] rowCnt = new int[m], colCnt = new int[n];
        for (int i = 0; i < arr.length; i++) {
            int r = posR[arr[i]], c = posC[arr[i]];
            rowCnt[r]++;
            colCnt[c]++;
            if (rowCnt[r] == n || colCnt[c] == m) return i;
        }
        return -1;
    }
}
