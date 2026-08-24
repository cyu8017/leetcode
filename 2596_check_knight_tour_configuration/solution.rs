// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

impl Solution {
    pub fn check_valid_grid(grid: Vec<Vec<i32>>) -> bool {
        let n = grid.len();
        if grid[0][0] != 0 {
            return false;
        }
        let mut pos = vec![(0, 0); n * n];
        for i in 0..n {
            for j in 0..n {
                pos[grid[i][j] as usize] = (i as i32, j as i32);
            }
        }
        let dirs = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ];
        for v in 0..n * n - 1 {
            let (r, c) = pos[v];
            let mut ok = false;
            for (dr, dc) in dirs {
                if r + dr == pos[v + 1].0 && c + dc == pos[v + 1].1 {
                    ok = true;
                    break;
                }
            }
            if !ok {
                return false;
            }
        }
        true
    }
}
