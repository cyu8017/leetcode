// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> floodFill(std::vector<std::vector<int>>& image, int sr, int sc, int color) {
        int original = image[sr][sc];
        if (original == color) {
            return image;
        }
        dfs(image, sr, sc, original, color);
        return image;
    }

private:
    void dfs(std::vector<std::vector<int>>& image, int r, int c, int original, int color) {
        if (r < 0 || r >= static_cast<int>(image.size()) || c < 0 ||
            c >= static_cast<int>(image[0].size()) || image[r][c] != original) {
            return;
        }
        image[r][c] = color;
        dfs(image, r + 1, c, original, color);
        dfs(image, r - 1, c, original, color);
        dfs(image, r, c + 1, original, color);
        dfs(image, r, c - 1, original, color);
    }
};
