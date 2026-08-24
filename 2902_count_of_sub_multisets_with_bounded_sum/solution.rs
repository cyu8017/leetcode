// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

use std::collections::HashMap;

impl Solution {
    pub fn count_sub_multisets(nums: Vec<i32>, l: i32, mut r: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut total = 0i32;
        for v in nums {
            *freq.entry(v).or_insert(0) += 1;
            total += v;
        }
        if total < l {
            return 0;
        }
        if r > total {
            r = total;
        }
        let mut dp = vec![0i32; r as usize + 1];
        dp[0] = 1;
        let zeros = *freq.get(&0).unwrap_or(&0);
        freq.remove(&0);
        for (v, c) in freq {
            let mut ndp = vec![0i32; r as usize + 1];
            for sum in 0..=r as usize {
                if dp[sum] == 0 {
                    continue;
                }
                let mut k = 0i32;
                while k <= c && sum + (k * v) as usize <= r as usize {
                    let idx = sum + (k * v) as usize;
                    ndp[idx] = (ndp[idx] + dp[sum]) % MOD;
                    k += 1;
                }
            }
            dp = ndp;
        }
        let mut ans = 0i32;
        for s in l..=r {
            ans = (ans + dp[s as usize]) % MOD;
        }
        ((ans as i64) * (zeros as i64 + 1) % MOD as i64) as i32
    }
}
