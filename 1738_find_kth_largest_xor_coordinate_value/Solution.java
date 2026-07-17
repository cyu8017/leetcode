// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

import java.util.Arrays;

class Solution {
    public int kthLargestValue(int[][] matrix, int k) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] pref = new int[rows + 1][cols + 1];
        int[] values = new int[rows * cols];
        int index = 0;
        for (int r = 1; r <= rows; r++) {
            for (int c = 1; c <= cols; c++) {
                pref[r][c] = pref[r - 1][c] ^ pref[r][c - 1] ^ pref[r - 1][c - 1] ^ matrix[r - 1][c - 1];
                values[index++] = pref[r][c];
            }
        }
        Arrays.sort(values);
        return values[values.length - k];
    }
}
