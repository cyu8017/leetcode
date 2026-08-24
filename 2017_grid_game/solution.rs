// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

impl Solution {
    pub fn grid_game(grid: Vec<Vec<i32>>) -> i64 {
        let n = grid[0].len();
        let mut top: i64 = grid[0].iter().map(|&v| v as i64).sum();
        let mut bottom = 0i64;
        let mut ans = i64::MAX;
        for i in 0..n {
            top -= grid[0][i] as i64;
            ans = ans.min(top.max(bottom));
            bottom += grid[1][i] as i64;
        }
        ans
    }
}
