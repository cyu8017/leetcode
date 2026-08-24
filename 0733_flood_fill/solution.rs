// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

impl Solution {
    pub fn flood_fill(mut image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {
        let original = image[sr as usize][sc as usize];
        if original != color {
            Self::dfs(&mut image, sr, sc, original, color);
        }
        image
    }

    fn dfs(image: &mut [Vec<i32>], r: i32, c: i32, original: i32, color: i32) {
        if r < 0
            || r >= image.len() as i32
            || c < 0
            || c >= image[0].len() as i32
            || image[r as usize][c as usize] != original
        {
            return;
        }
        image[r as usize][c as usize] = color;
        Self::dfs(image, r + 1, c, original, color);
        Self::dfs(image, r - 1, c, original, color);
        Self::dfs(image, r, c + 1, original, color);
        Self::dfs(image, r, c - 1, original, color);
    }
}
