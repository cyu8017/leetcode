// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

impl Solution {
    pub fn sum_of_power(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let k = k as usize;
        let mut f = vec![vec![0i64; k + 1]; n + 1];
        f[0][0] = 1;
        for i in 1..=n {
            let x = nums[i - 1] as usize;
            for j in 0..=k {
                f[i][j] = (f[i - 1][j] * 2) % MOD;
                if j >= x {
                    f[i][j] = (f[i][j] + f[i - 1][j - x]) % MOD;
                }
            }
        }
        f[n][k] as i32
    }
}
