// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

class Solution {
    public int numSubmat(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] heights = new int[n];
        int ans = 0;

        for (int[] row : mat) {
            for (int j = 0; j < n; j++) {
                heights[j] = row[j] == 1 ? heights[j] + 1 : 0;
            }
            int running = 0;
            int[][] stack = new int[n][2];
            int top = -1;
            for (int h : heights) {
                int count = 1;
                while (top >= 0 && stack[top][0] >= h) {
                    int[] prev = stack[top--];
                    running -= prev[0] * prev[1];
                    count += prev[1];
                }
                stack[++top] = new int[] { h, count };
                running += h * count;
                ans += running;
            }
        }
        return ans;
    }
}
