// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

impl Solution {
    pub fn sum_of_blocks(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut ans = 0i32;
        let mut k = 1i32;
        for i in 1..=n {
            let mut x = 1i64;
            for j in k..k + i {
                x = x * j as i64 % MOD;
            }
            ans = ((ans as i64 + x) % MOD) as i32;
            k += i;
        }
        ans
    }
}
