// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

class Solution {
    func floodFill(_ image: [[Int]], _ sr: Int, _ sc: Int, _ color: Int) -> [[Int]] {
        var image = image
        let old = image[sr][sc]
        if old == color { return image }
        let m = image.count, n = image[0].count
        func dfs(_ r: Int, _ c: Int) {
            if r < 0 || r >= m || c < 0 || c >= n || image[r][c] != old { return }
            image[r][c] = color
            dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)
        }
        dfs(sr, sc)
        return image
    }
}
