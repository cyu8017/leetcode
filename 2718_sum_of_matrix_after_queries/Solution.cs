// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

public class Solution {
    public long MatrixSumQueries(int n, int[][] queries) {
        bool[] rowDone = new bool[n], colDone = new bool[n];
        int rowsLeft = n, colsLeft = n;
        long ans = 0;
        for (int i = queries.Length - 1; i >= 0; i--) {
            int type = queries[i][0], idx = queries[i][1], val = queries[i][2];
            if (type == 0) {
                if (!rowDone[idx]) {
                    ans += 1L * val * colsLeft;
                    rowDone[idx] = true;
                    rowsLeft--;
                }
            } else {
                if (!colDone[idx]) {
                    ans += 1L * val * rowsLeft;
                    colDone[idx] = true;
                    colsLeft--;
                }
            }
        }
        return ans;
    }
}
