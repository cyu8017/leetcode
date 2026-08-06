// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

impl Solution {
    pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let mut dp = grid[0].clone();
        for row in &grid[1..] {
            let first = (0..dp.len()).min_by_key(|&i| dp[i]).unwrap();
            let second_value = dp
                .iter()
                .enumerate()
                .filter(|(i, _)| *i != first)
                .map(|(_, &v)| v)
                .min()
                .unwrap_or(0);
            let mut nxt = vec![0; row.len()];
            for (i, &value) in row.iter().enumerate() {
                nxt[i] = value + if i == first { second_value } else { dp[first] };
            }
            dp = nxt;
        }
        *dp.iter().min().unwrap()
    }
}
