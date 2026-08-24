// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

class Solution {
    fun floodFill(image: Array<IntArray>, sr: Int, sc: Int, color: Int): Array<IntArray> {
        var original = image[sr][sc]
        if (original == color) return image
        dfs(image, sr, sc, original, color)
        return image
    }

    private fun dfs(image: Array<IntArray>, r: Int, c: Int, original: Int, color: Int) {
        if (r < 0 || r >= image.size || c < 0 || c >= image[0].size || image[r][c] != original) return
        image[r][c] = color
        dfs(image, r + 1, c, original, color)
        dfs(image, r - 1, c, original, color)
        dfs(image, r, c + 1, original, color)
        dfs(image, r, c - 1, original, color)
    }
}
