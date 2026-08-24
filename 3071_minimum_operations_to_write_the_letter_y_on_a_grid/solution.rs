// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

impl Solution {
    pub fn minimum_operations_to_write_y(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len() as i32;
        let mut cnt1 = [0i32; 3];
        let mut cnt2 = [0i32; 3];
        for i in 0..n {
            for j in 0..n {
                let x = grid[i as usize][j as usize] as usize;
                let a = i == j && i <= n / 2;
                let b = i + j == n - 1 && i <= n / 2;
                let c = j == n / 2 && i >= n / 2;
                if a || b || c {
                    cnt1[x] += 1;
                } else {
                    cnt2[x] += 1;
                }
            }
        }
        let mut ans = n * n;
        for i in 0..3 {
            for j in 0..3 {
                if i != j {
                    ans = ans.min(n * n - cnt1[i] - cnt2[j]);
                }
            }
        }
        ans
    }
}
