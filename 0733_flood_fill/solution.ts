// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

export function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    const original = image[sr][sc];
    if (original === color) return image;
    const dfs = (r, c) => {
        if (r < 0 || r >= image.length || c < 0 || c >= image[0].length || image[r][c] !== original) return;
        image[r][c] = color;
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    };
    dfs(sr, sc);
    return image;
}
