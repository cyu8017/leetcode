// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

impl Solution {
    const N: usize = 31;
    const MOD: i64 = 1_000_000_007;

    fn qpow(mut a: i64, mut k: i64) -> i64 {
        let mut res = 1i64;
        while k > 0 {
            if k & 1 == 1 {
                res = res * a % Self::MOD;
            }
            a = a * a % Self::MOD;
            k >>= 1;
        }
        res
    }

    pub fn magical_sum(m: i32, k: i32, nums: Vec<i32>) -> i32 {
        let mut f = vec![0i64; Self::N];
        let mut g = vec![0i64; Self::N];
        f[0] = 1;
        g[0] = 1;
        for i in 1..Self::N {
            f[i] = f[i - 1] * i as i64 % Self::MOD;
            g[i] = Self::qpow(f[i], Self::MOD - 2);
        }
        let comb = |mm: i32, nn: i32| -> i64 {
            if nn < 0 || nn > mm {
                return 0;
            }
            f[mm as usize] * g[nn as usize] % Self::MOD * g[(mm - nn) as usize] % Self::MOD
        };
        let n = nums.len();
        let m = m as usize;
        let k = k as usize;
        let mut dp = vec![vec![vec![vec![-1i64; Self::N]; k + 1]; m + 1]; n + 1];
        fn dfs(
            i: usize,
            j: i32,
            kk: i32,
            st: usize,
            n: usize,
            nums: &[i32],
            dp: &mut [Vec<Vec<Vec<i64>>>],
            comb: &dyn Fn(i32, i32) -> i64,
        ) -> i64 {
            if kk < 0 || (i == n && j > 0) {
                return 0;
            }
            if i == n {
                let mut kk = kk;
                let mut st = st;
                while st > 0 {
                    kk -= (st & 1) as i32;
                    st >>= 1;
                }
                return if kk == 0 { 1 } else { 0 };
            }
            if dp[i][j as usize][kk as usize][st] != -1 {
                return dp[i][j as usize][kk as usize][st];
            }
            let mut res = 0i64;
            for t in 0..=j {
                let nt = t as usize + st;
                let nk = kk - (nt & 1) as i32;
                let p = Solution::qpow(nums[i] as i64, t as i64);
                let tmp = comb(j, t) * p % Solution::MOD
                    * dfs(i + 1, j - t, nk, nt >> 1, n, nums, dp, comb)
                    % Solution::MOD;
                res = (res + tmp) % Solution::MOD;
            }
            dp[i][j as usize][kk as usize][st] = res;
            res
        }
        dfs(0, m as i32, k as i32, 0, n, &nums, &mut dp, &comb) as i32
    }
}
