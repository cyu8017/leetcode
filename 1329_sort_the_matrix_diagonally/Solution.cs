// LeetCode 1329 - Sort The Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

using System.Collections.Generic;

public class Solution {
    public int[][] DiagonalSort(int[][] mat) {
        var diagonals = new Dictionary<int, List<int>>();
        for (int r = 0; r < mat.Length; r++) {
            for (int c = 0; c < mat[r].Length; c++) {
                int key = r - c;
                if (!diagonals.ContainsKey(key)) diagonals[key] = new List<int>();
                diagonals[key].Add(mat[r][c]);
            }
        }
        foreach (var values in diagonals.Values) values.Sort((a, b) => b.CompareTo(a));
        for (int r = 0; r < mat.Length; r++) {
            for (int c = 0; c < mat[r].Length; c++) {
                var list = diagonals[r - c];
                mat[r][c] = list[list.Count - 1];
                list.RemoveAt(list.Count - 1);
            }
        }
        return mat;
    }
}
