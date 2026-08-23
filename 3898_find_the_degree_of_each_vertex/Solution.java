// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

class Solution {
    public int[] findDegrees(int[][] matrix) {
        var ans = new int[matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            for (int x : matrix[i]) ans[i] += x;
        }
        return ans;
    }
}
