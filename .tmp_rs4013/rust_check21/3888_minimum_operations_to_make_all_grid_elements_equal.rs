struct Solution;
// LeetCode 3888 - Minimum Operations to Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, k: i32) -> i64 {
        let m = grid.len();
        let n = grid[0].len();
        let max_val = grid.iter().flat_map(|row| row.iter()).copied().max().unwrap();
        let check = |target: i32| -> i64 {
            let mut diff = vec![vec![0i64; n + 2]; m + 2];
            let mut total_ops = 0i64;
            for i in 1..=m {
                for j in 1..=n {
                    diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
                    let cur_val = grid[i - 1][j - 1] as i64 + diff[i][j];
                    if cur_val > target as i64 {
                        return -1;
                    }
                    if cur_val < target as i64 {
                        if i + k as usize - 1 > m || j + k as usize - 1 > n {
                            return -1;
                        }
                        let needed = target as i64 - cur_val;
                        total_ops += needed;
                        diff[i][j] += needed;
                        diff[i + k as usize][j] -= needed;
                        diff[i][j + k as usize] -= needed;
                        diff[i + k as usize][j + k as usize] += needed;
                    }
                }
            }
            total_ops
        };
        for t in max_val..=max_val + 1 {
            let res = check(t);
            if res != -1 {
                return res;
            }
        }
        -1
    }
}
