// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

impl Solution {
    pub fn maximum_xor_product(mut a: i64, mut b: i64, n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        for i in (0..n).rev() {
            let bit = 1i64 << i;
            let abit = a & bit;
            let bbit = b & bit;
            if abit == bbit {
                a |= bit;
                b |= bit;
            } else if a > b {
                b |= bit;
                a &= !bit;
            } else {
                a |= bit;
                b &= !bit;
            }
        }
        ((a % MOD) * (b % MOD) % MOD) as i32
    }
}
