// LeetCode 3850 - Count Sequences to K
// https://leetcode.com/problems/count-sequences-to-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_sequences(nums: Vec<i32>, k: i64) -> i32 {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        fn dfs(
            i: usize,
            p: i64,
            q: i64,
            nums: &[i32],
            k: i64,
            memo: &mut HashMap<(usize, i64, i64), i32>,
        ) -> i32 {
            if i == nums.len() {
                return if p == k && q == 1 { 1 } else { 0 };
            }
            if let Some(&v) = memo.get(&(i, p, q)) {
                return v;
            }
            let mut res = dfs(i + 1, p, q, nums, k, memo);
            let x = nums[i] as i64;
            let g1 = gcd(p * x, q);
            res += dfs(i + 1, (p * x) / g1, q / g1, nums, k, memo);
            let g2 = gcd(p, q * x);
            res += dfs(i + 1, p / g2, (q * x) / g2, nums, k, memo);
            memo.insert((i, p, q), res);
            res
        }
        dfs(0, 1, 1, &nums, k, &mut HashMap::new())
    }
}
