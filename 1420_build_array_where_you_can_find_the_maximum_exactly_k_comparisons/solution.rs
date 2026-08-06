// LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
// https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

impl Solution {
    pub fn num_of_arrays(n: i32, m: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let (n, m, k) = (n as usize, m as usize, k as usize);
        let mut dp = vec![vec![0i64; m + 1]; k + 1];
        for maximum in 1..=m {
            dp[1][maximum] = 1;
        }
        for _ in 1..n {
            let mut nxt = vec![vec![0i64; m + 1]; k + 1];
            for cost in 1..=k {
                let mut prefix = 0i64;
                for maximum in 1..=m {
                    prefix = (prefix + dp[cost - 1][maximum - 1]) % MOD;
                    nxt[cost][maximum] = (maximum as i64 * dp[cost][maximum] + prefix) % MOD;
                }
            }
            dp = nxt;
        }
        (dp[k].iter().sum::<i64>() % MOD) as i32
    }
}
