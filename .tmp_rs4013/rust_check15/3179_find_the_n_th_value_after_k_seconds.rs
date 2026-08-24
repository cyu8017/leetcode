struct Solution;
// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

impl Solution {
    pub fn value_after_k_seconds(n: i32, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = n as usize;
        let mut a = vec![1; n];
        for _ in 0..k {
            for i in 1..n {
                a[i] = (a[i] + a[i - 1]) % MOD;
            }
        }
        a[n - 1]
    }
}

fn main() {}
