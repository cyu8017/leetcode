// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

impl Solution {
    pub fn find_column_width(grid: Vec<Vec<i32>>) -> Vec<i32> {
        fn width(x: i32) -> i32 {
            if x == 0 {
                return 1;
            }
            let mut w = 0;
            let mut x = x as i64;
            if x < 0 {
                w += 1;
                x = -x;
            }
            while x > 0 {
                w += 1;
                x /= 10;
            }
            w
        }
        let n = grid[0].len();
        let mut ans = vec![0; n];
        for row in &grid {
            for j in 0..n {
                let w = width(row[j]);
                if w > ans[j] {
                    ans[j] = w;
                }
            }
        }
        ans
    }
}
