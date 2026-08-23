// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

public class Solution {
    public int KthLargestValue(int[][] matrix, int k) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        var pref = new int[rows + 1, cols + 1];
        var values = new int[rows * cols];
        int index = 0;
        for (int r = 1; r <= rows; r++) {
            for (int c = 1; c <= cols; c++) {
                pref[r, c] = pref[r - 1, c] ^ pref[r, c - 1] ^ pref[r - 1, c - 1] ^ matrix[r - 1][c - 1];
                values[index++] = pref[r, c];
            }
        }
        Array.Sort(values);
        return values[values.Length - k];
    }
}
