// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

impl Solution {
    pub fn max_jumps(arr: Vec<i32>, d: i32) -> i32 {
        let n = arr.len();
        let d = d as i32;
        let mut dp = vec![1; n];
        let mut order: Vec<usize> = (0..n).collect();
        order.sort_by_key(|&i| arr[i]);
        for i in order {
            for step in [-1i32, 1] {
                let mut j = i as i32 + step;
                while j >= 0
                    && (j as usize) < n
                    && (j - i as i32).abs() <= d
                    && arr[j as usize] < arr[i]
                {
                    dp[i] = dp[i].max(1 + dp[j as usize]);
                    j += step;
                }
            }
        }
        *dp.iter().max().unwrap()
    }
}
