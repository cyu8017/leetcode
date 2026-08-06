// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

impl Solution {
    pub fn count_sub_islands(grid1: Vec<Vec<i32>>, mut grid2: Vec<Vec<i32>>) -> i32 {
        let rows = grid2.len();
        let cols = grid2[0].len();

        fn dfs(grid1: &Vec<Vec<i32>>, grid2: &mut Vec<Vec<i32>>, r: i32, c: i32) -> bool {
            let rows = grid2.len() as i32;
            let cols = grid2[0].len() as i32;
            if r < 0 || c < 0 || r >= rows || c >= cols || grid2[r as usize][c as usize] == 0 {
                return true;
            }
            grid2[r as usize][c as usize] = 0;
            let mut ok = grid1[r as usize][c as usize] == 1;
            for (nr, nc) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] {
                if !dfs(grid1, grid2, nr, nc) {
                    ok = false;
                }
            }
            ok
        }

        let mut ans = 0;
        for r in 0..rows {
            for c in 0..cols {
                if grid2[r][c] == 1 && dfs(&grid1, &mut grid2, r as i32, c as i32) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
