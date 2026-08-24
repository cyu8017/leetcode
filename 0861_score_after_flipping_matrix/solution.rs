// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

impl Solution {
    pub fn matrix_score(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        for row in &mut grid {
            if row[0] == 0 {
                for x in row.iter_mut() {
                    *x ^= 1;
                }
            }
        }
        let mut ans = m as i32 * (1 << (n - 1));
        for j in 1..n {
            let ones: i32 = (0..m).map(|i| grid[i][j]).sum();
            ans += ones.max(m as i32 - ones) * (1 << (n - 1 - j));
        }
        ans
    }
}
