// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

impl Solution {
    pub fn minimum_area(grid: Vec<Vec<i32>>) -> i32 {
        let mut x1 = grid.len() as i32;
        let mut y1 = grid[0].len() as i32;
        let mut x2 = 0;
        let mut y2 = 0;
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j] == 1 {
                    x1 = x1.min(i as i32);
                    y1 = y1.min(j as i32);
                    x2 = x2.max(i as i32);
                    y2 = y2.max(j as i32);
                }
            }
        }
        (x2 - x1 + 1) * (y2 - y1 + 1)
    }
}
