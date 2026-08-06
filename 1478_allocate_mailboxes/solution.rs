// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

impl Solution {
    pub fn min_distance(mut houses: Vec<i32>, k: i32) -> i32 {
        houses.sort_unstable();
        let n = houses.len();
        let mut cost = vec![vec![0; n]; n];
        for i in 0..n {
            for j in i..n {
                let mid = houses[(i + j) / 2];
                cost[i][j] = (i..=j).map(|t| (houses[t] - mid).abs()).sum();
            }
        }
        let mut dp = vec![0i32];
        dp.extend(std::iter::repeat(i32::MAX / 4).take(n));
        for _ in 0..k {
            let mut ndp = vec![0i32];
            ndp.extend(std::iter::repeat(i32::MAX / 4).take(n));
            for j in 1..=n {
                ndp[j] = (0..j).map(|i| dp[i].saturating_add(cost[i][j - 1])).min().unwrap();
            }
            dp = ndp;
        }
        dp[n]
    }
}
