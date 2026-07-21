// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

impl Solution {
    pub fn rotate_the_box(box_grid: Vec<Vec<char>>) -> Vec<Vec<char>> {
        let m = box_grid.len();
        let n = box_grid[0].len();
        let mut rotated = vec![vec!['.'; m]; n];
        for i in 0..n {
            for j in 0..m {
                rotated[i][j] = box_grid[m - 1 - j][i];
            }
        }
        for col in 0..m {
            let mut row = n as i32 - 1;
            for i in (0..n).rev() {
                if rotated[i][col] == '*' {
                    row = i as i32 - 1;
                } else if rotated[i][col] == '#' {
                    rotated[i][col] = '.';
                    rotated[row as usize][col] = '#';
                    row -= 1;
                }
            }
        }
        rotated
    }
}
