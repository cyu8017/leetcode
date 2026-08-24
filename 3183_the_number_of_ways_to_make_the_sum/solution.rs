// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

impl Solution {
    pub fn number_of_ways(n: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let coins = [1, 2, 6];
        let n = n as usize;
        let mut f = vec![0; n + 1];
        f[0] = 1;
        for &x in &coins {
            for j in x..=n {
                f[j] = (f[j] + f[j - x]) % MOD;
            }
        }
        let mut ans = f[n];
        if n >= 4 {
            ans = (ans + f[n - 4]) % MOD;
        }
        if n >= 8 {
            ans = (ans + f[n - 8]) % MOD;
        }
        ans
    }
}
