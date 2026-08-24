// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

use std::collections::HashMap;

impl Solution {
    pub fn xor_after_queries(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut by_k: HashMap<i32, Vec<(i32, i32, i32, i32)>> = HashMap::new();
        for q in queries {
            by_k.entry(q[2]).or_default().push((q[0], q[1], q[2], q[3]));
        }
        let mut res = nums;
        for (k, ups) in by_k {
            let mut fac = vec![1i32; n];
            for (l, r, _, v) in ups {
                let mut i = l as usize;
                let r = r as usize;
                let step = k as usize;
                while i <= r {
                    fac[i] = ((fac[i] as i64 * v as i64) % MOD) as i32;
                    i += step;
                }
            }
            for i in 0..n {
                res[i] = ((res[i] as i64 * fac[i] as i64) % MOD) as i32;
            }
        }
        let mut ans = 0;
        for v in res {
            ans ^= v;
        }
        ans
    }
}
