// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

use std::collections::BTreeMap;

impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut sl: BTreeMap<i32, i32> = BTreeMap::new();
        let n = nums.len();
        let mut f = vec![0i32; n + 1];
        let mut g = vec![0i32; n + 1];
        f[0] = 1;
        g[0] = 1;
        let mut l = 1usize;
        for r in 1..=n {
            *sl.entry(nums[r - 1]).or_insert(0) += 1;
            while sl.iter().next_back().unwrap().0 - sl.iter().next().unwrap().0 > k {
                let key = nums[l - 1];
                if let Some(c) = sl.get_mut(&key) {
                    *c -= 1;
                    if *c == 0 {
                        sl.remove(&key);
                    }
                }
                l += 1;
            }
            f[r] = g[r - 1];
            if l >= 2 {
                f[r] = (f[r] - g[l - 2] + MOD) % MOD;
            }
            g[r] = (g[r - 1] + f[r]) % MOD;
        }
        f[n]
    }
}
