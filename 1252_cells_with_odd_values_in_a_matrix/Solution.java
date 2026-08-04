// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[] rows = new int[m], cols = new int[n];
        for (int[] idx : indices) {
            rows[idx[0]] ^= 1;
            cols[idx[1]] ^= 1;
        }
        int answer = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                answer += (rows[r] ^ cols[c]);
            }
        }
        return answer;
    }
}

