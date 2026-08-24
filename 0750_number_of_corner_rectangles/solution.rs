// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

impl Solution {
    pub fn count_corner_rectangles(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0;
        for i in 0..m {
            for j in i + 1..m {
                let mut count = 0;
                for c in 0..n {
                    if grid[i][c] != 0 && grid[j][c] != 0 {
                        count += 1;
                    }
                }
                ans += count * (count - 1) / 2;
            }
        }
        ans
    }
}
