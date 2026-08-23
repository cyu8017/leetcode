// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        int original = image[sr][sc];
        if (original == color) return image;
        Dfs(image, sr, sc, original, color);
        return image;
    }

    private void Dfs(int[][] image, int r, int c, int original, int color) {
        if (r < 0 || r >= image.Length || c < 0 || c >= image[0].Length || image[r][c] != original) return;
        image[r][c] = color;
        Dfs(image, r + 1, c, original, color);
        Dfs(image, r - 1, c, original, color);
        Dfs(image, r, c + 1, original, color);
        Dfs(image, r, c - 1, original, color);
    }
}
