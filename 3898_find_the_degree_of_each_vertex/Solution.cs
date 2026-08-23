// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

public class Solution {
    public int[] FindDegrees(int[][] matrix) {
        var ans = new int[matrix.Length];
        for (int i = 0; i < matrix.Length; i++) {
            foreach (int x in matrix[i]) ans[i] += x;
        }
        return ans;
    }
}
