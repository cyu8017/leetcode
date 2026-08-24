// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let k = k as usize;
        let sum: i64 = nums.iter().map(|&x| x as i64).sum();
        if sum < 2 * k as i64 {
            return 0;
        }
        let mut dp = vec![0i64; k];
        dp[0] = 1;
        for &x in &nums {
            let x = x as usize;
            for s in (x..k).rev() {
                dp[s] = (dp[s] + dp[s - x]) % MOD;
            }
        }
        let bad: i64 = dp.iter().sum::<i64>() % MOD;
        let mut total = 1i64;
        for _ in 0..nums.len() {
            total = total * 2 % MOD;
        }
        ((total - 2 * bad % MOD + MOD) % MOD) as i32
    }
}
