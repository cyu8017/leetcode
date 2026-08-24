// LeetCode 3855 - Sum of K Digit Numbers in a Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

impl Solution {
    pub fn sum_of_numbers(l: i32, r: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn qpow(mut a: i64, mut n: i64, m: i64) -> i64 {
            a %= m;
            let mut ans = 1;
            while n > 0 {
                if n & 1 == 1 {
                    ans = ans * a % m;
                }
                a = a * a % m;
                n >>= 1;
            }
            ans
        }
        let n = (r - l + 1) as i64;
        let sum = (l as i64 + r as i64) * n / 2 % MOD;
        let part1 = qpow(n % MOD, (k - 1) as i64, MOD);
        let part2 = (qpow(10, k as i64, MOD) - 1 + MOD) % MOD;
        let inv9 = qpow(9, MOD - 2, MOD);
        let mut ans = sum;
        ans = ans * part1 % MOD;
        ans = ans * part2 % MOD;
        ans = ans * inv9 % MOD;
        ans as i32
    }
}
