// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

impl Solution {
    pub fn largest1_bordered_square(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut hor = vec![vec![0; n]; m];
        let mut ver = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    hor[i][j] = if j > 0 { hor[i][j - 1] + 1 } else { 1 };
                    ver[i][j] = if i > 0 { ver[i - 1][j] + 1 } else { 1 };
                }
            }
        }
        for side in (1..=m.min(n)).rev() {
            for i in (side - 1)..m {
                for j in (side - 1)..n {
                    if hor[i][j] >= side as i32
                        && ver[i][j] >= side as i32
                        && hor[i + 1 - side][j] >= side as i32
                        && ver[i][j + 1 - side] >= side as i32
                    {
                        return (side * side) as i32;
                    }
                }
            }
        }
        0
    }
}
