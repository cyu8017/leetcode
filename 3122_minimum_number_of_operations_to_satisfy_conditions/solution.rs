// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

impl Solution {
    pub fn minimum_operations(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const INF: i32 = 1 << 29;
        let mut f = vec![vec![INF; 10]; n];
        for i in 0..n {
            let mut cnt = [0i32; 10];
            for j in 0..m {
                cnt[grid[j][i] as usize] += 1;
            }
            if i == 0 {
                for j in 0..10 {
                    f[i][j] = m as i32 - cnt[j];
                }
            } else {
                for j in 0..10 {
                    for k in 0..10 {
                        if j != k {
                            f[i][j] = f[i][j].min(f[i - 1][k] + m as i32 - cnt[j]);
                        }
                    }
                }
            }
        }
        *f[n - 1].iter().min().unwrap()
    }
}
