// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

impl Solution {
    pub fn shift_grid(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut flat: Vec<i32> = grid.into_iter().flatten().collect();
        let len = flat.len();
        let k = (k as usize) % len;
        if k > 0 {
            flat.rotate_right(k);
        }
        flat.chunks(n).map(|c| c.to_vec()).collect()
    }
}
