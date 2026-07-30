// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

public class Solution {
    public int OddCells(int m, int n, int[][] indices) {
        var rows = new int[m];
        var cols = new int[n];
        foreach (var idx in indices) {
            rows[idx[0]] ^= 1;
            cols[idx[1]] ^= 1;
        }
        int answer = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if ((rows[r] ^ cols[c]) == 1) answer++;
            }
        }
        return answer;
    }
}
