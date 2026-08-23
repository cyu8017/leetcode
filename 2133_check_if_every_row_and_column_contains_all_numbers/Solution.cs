// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

public class Solution {
    public bool CheckValid(int[][] matrix) {
        int n = matrix.Length;
        for (int i = 0; i < n; i++) {
            bool[] row = new bool[n + 1], col = new bool[n + 1];
            for (int j = 0; j < n; j++) {
                if (row[matrix[i][j]] || col[matrix[j][i]]) return false;
                row[matrix[i][j]] = col[matrix[j][i]] = true;
            }
        }
        return true;
    }
}
