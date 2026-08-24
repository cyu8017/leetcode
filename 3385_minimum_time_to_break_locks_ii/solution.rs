// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

impl Solution {
    fn bits_ones(mut x: i32) -> i32 {
        let mut c = 0;
        while x > 0 {
            c += x & 1;
            x >>= 1;
        }
        c
    }

    pub fn find_minimum_time(strength: Vec<i32>) -> i32 {
        let n = strength.len();
        let nmask = 1 << n;
        const INF: i64 = 10i64.pow(18);
        let mut dp = vec![INF; nmask];
        dp[0] = 0;
        let k = 1;
        for mask in 0..nmask {
            if dp[mask] == INF {
                continue;
            }
            let opened = Self::bits_ones(mask as i32);
            let x = 1 + opened * k;
            for i in 0..n {
                if mask & (1 << i) != 0 {
                    continue;
                }
                let t = (strength[i] + x - 1) / x;
                let nmask2 = mask | (1 << i);
                if dp[mask] + (t as i64) < dp[nmask2] {
                    dp[nmask2] = dp[mask] + t as i64;
                }
            }
        }
        dp[nmask - 1] as i32
    }
}
