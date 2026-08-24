// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

impl Solution {
    fn gcd(mut a: i32, mut b: i32) -> i32 {
        if a == 0 {
            return b;
        }
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }

    pub fn subsequence_pair_count(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let max_v = *nums.iter().max().unwrap() as usize;
        let mut dp = vec![vec![0i32; max_v + 1]; max_v + 1];
        dp[0][0] = 1;
        for x in nums {
            let mut ndp = dp.clone();
            for a in 0..=max_v {
                for b in 0..=max_v {
                    if dp[a][b] == 0 {
                        continue;
                    }
                    let na = if a == 0 { x as usize } else { Self::gcd(a as i32, x) as usize };
                    let nb = if b == 0 { x as usize } else { Self::gcd(b as i32, x) as usize };
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % MOD;
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % MOD;
                }
            }
            dp = ndp;
        }
        let mut ans = 0;
        for g in 1..=max_v {
            ans = (ans + dp[g][g]) % MOD;
        }
        ans
    }
}
