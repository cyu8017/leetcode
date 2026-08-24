// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

impl Solution {
    pub fn maximum_cost(n: i32, highways: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = n as usize;
        if k + 1 > n as i32 {
            return -1;
        }
        let mut g = vec![Vec::new(); n];
        for h in highways {
            g[h[0] as usize].push((h[1] as usize, h[2]));
            g[h[1] as usize].push((h[0] as usize, h[2]));
        }
        let mut dp = vec![vec![-1; n]; 1 << n];
        for i in 0..n {
            dp[1 << i][i] = 0;
        }
        let mut ans = -1;
        for mask in 0..(1 << n) {
            let cities = mask.count_ones() as i32;
            for u in 0..n {
                if dp[mask][u] < 0 {
                    continue;
                }
                if cities - 1 == k {
                    ans = ans.max(dp[mask][u]);
                }
                for &(v, w) in &g[u] {
                    if mask & (1 << v) != 0 {
                        continue;
                    }
                    let nm = mask | (1 << v);
                    dp[nm][v] = dp[nm][v].max(dp[mask][u] + w);
                }
            }
        }
        ans
    }
}
