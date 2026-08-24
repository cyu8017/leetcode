struct Solution;
// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

impl Solution {
    pub fn count_distinct_strings(s: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len() as i32;
        let mut ans = 1i64;
        for _ in 0..n - k + 1 {
            ans = ans * 2 % MOD;
        }
        ans as i32
    }
}

fn main() {}
